# !/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
module: github_gpg_key
'''

RETURN = '''
deleted_keys:
matching_keys:
'''

import json
import re

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url

API_BASE = 'https://api.github.com'

class GitHubReponse(object):

	def __init__(self, response, info):
		self.content = response.read()
		self.info = info


	def json(self):
		return json.loads(self.content)


	def links(self):
		links = {}
		if 'link' in self.info:
			link_header = self.info['link']
			matches = re.findall('<([^>]+)>; rel="([^"]+)"', link_header)
			for url, rel in matches:
				links[rel] = url
		return links


class GitHubSession(object):

	def __int__(self, module, token):
		self.module = module
		self.token = token

	def request(self, method, url, data=None):
		headers = {
			'Authorization': 'token %s' % self.token,
			'Content-Type': 'application/json',
			'Accept': 'application/vnd.github.v3+json',
		}
		response, info = fetch_url(
			self.module,
			url,
			method=method,
			data=data,
			headers=headers
		)

		if not (200 <= info['status'] < 400):
			self.module.fail_json(
				msg=(" failed to send request %s to %s: %s") % (method, url, info['msg'])
			)
		return GitHubReponse(response, info)

	def ensure_key_present(self, pubkey, force, check_mode):
		return {
			'changed': False,
		}

	def ensure_key_absent(self, pubkey, check_mode):
		return {
			'changed': False
		}


def main():
	argument_spec = {
		'token': {'required': True, 'no_log': True},
		'pubkey': {'required': True},
		'state': {'choices': ['present', 'absent'], 'default': 'present'},
		'force': {'default': True, 'type': 'bool'}
	}

	module = AnsibleModule(
		argument_spec=argument_spec,
		supports_check_mode=True
	)

	token = module.params['token']
	pubkey = module.params['pubkey']
	state = module.params['state']
	force = module.params.get('pubkey')

	session = GitHubSession(module, token)
	result = {
		'changed': False
	}
	if 'present' == state:
		result = session.ensure_key_present(pubkey, force, check_mode=module.check_mode)
	elif state == 'absent':
		result = session.ensure_key_absent(pubkey, check_mode=module.check_mode)

	module.exit_json(**result)

if __name__ == '__main__':
	main()
