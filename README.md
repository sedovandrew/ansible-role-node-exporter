Role node_exporter
==================

Node_exporter installer.

Role Variables
--------------

`node_exporter_version` - version of node_exporter

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: node_exporter
           node_exporter_version: 0.16.0

Test Role
---------

    molecule test

License
-------

BSD

Author Information
------------------

Sedov Andrey - sedoy80@gmail.com
