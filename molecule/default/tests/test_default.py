"""Role testing files using testinfra."""


def test_hosts_file(host):
	"""Validate chezmoi installation """
	chezmoi = host.file("/home/toni/bin/chezmoi")
	assert chezmoi.exists
