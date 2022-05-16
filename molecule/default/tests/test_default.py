"""Role testing files using testinfra."""


def test_hosts_file(host):
	"""Validate /etc/hosts file."""
	rsa = host.file("/home/toni/.ssh/id_rsa")
	dsa = host.file("/home/toni/.ssh/id_dsa")

	assert rsa.exists
	assert rsa.user == "toni"
	assert rsa.group == "toni"

	assert dsa.exists
	assert dsa.user == "toni"
	assert dsa.group == "toni"
