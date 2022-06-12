Ansible Role: Chezmoi
=========
A role to install and configure your dotfiles with chezmoi.

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/kilip/ansible-role-chezmoi/CI?style=flat-square)](https://github.com/kilip/ansible-role-chezmoi/actions/workflows/ci.yml)

Requirements
------------
None.

Role Variables
--------------
```yaml
# your local machine username
chezmoi_user: "toni"

# your github repo url
chezmoi_repo: "git@github.com:username/repo.git"
```

Dependencies
------------
None.

Example Playbook
----------------
```yaml
- hosts: all
  roles:
    - role: kilip.chezmoi
```
License
-------

MIT

Author Information
------------------
This role was created in 2022 by [Anthonius Munthi](https://itstoni.com)

