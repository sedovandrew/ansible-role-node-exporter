import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_node_exporter_is_running(host):
    host.service("node_exporter").is_running


def test_node_exporter_is_enabled(host):
    host.service("node_exporter").is_enabled
