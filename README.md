# PIA - Package Installer for Ansible

> Like pip but for Ansible content, resilient content management that works
> fast, offline, with caching, compatible with multiple versions of ansible
> and a very friendly user interface.

This project aims to become an alternative to the current `ansible-galaxy`
command line tool, one that would address some shortcomings such as:

- Ability to run offline, especially when checking if current dependencies
  are up to date.
- Use caching similar to how pip does, so network access would be needed only
  if current data is not available locally.
- Be idempotent.

## Installation

```
pip3 install pia
```

## Usage

Please note that not all features are implemented yet.

```bash
# Install a collection
pia install namespace.collection_name
# should also accept aliases like `pip i ...`

# Install a collection archive from disk
pia install ./path/to/collection.tar.gz

# Uninstall a collection
pia uninstall namespace.collection_name

# List installed collections
pia list
```
