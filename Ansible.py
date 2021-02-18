Introduction
-------------
Ansible is a modern configuration management tool that facilitates the task of setting up
and maintaining remote servers.

Definitions
------------
Control Machine: a system where Ansible is installed and configured to connect and
execute commands on nodes.

Inventory File: a file that contains information about the servers Ansible controls.
typically located at /etc/ansible/hosts.

Playbook: a file containing a series of tasks to be executed on a remote server.

Role: a collection of playbooks and other files that are relevant to a goal such as
installing a web server.

Play: a full Ansible run. A play can have several playbooks and roles, included from
a single playbook that acts as entry point.

Ansible configuration
----------------------
Ansible supports several sources for configuring its behavior, including an ini
file named ansible.cfg
Changes can be made and used in a configuration file which will be searched for in
the following order:
1.ansible.cfg (in the current directory)
2.~/.ansible.cfg (in the home directory)
3./etc/ansible/ansible.cfg

Testing connectivity using a Custom Inventory File
---------------------------------------------------
$ ansible all -m ping -i my_custom_inventory

Executing a command on a node
-------------------------------
$ ansible all -a "uname -a"

Running Playbooks
-------------------
$ ansible-playbook myplaybook.yml

Getting Information about a Play
---------------------------------
$ ansible-playbook myplaybook.yml --list-tasks
$ ansible-playbook myplaybook.yml --list-hosts

Ansible modules
----------------
Ansible modules are standalone scripts that can be used on remote servers.
$ ansible-doc -l
to list all available modules.

$ ansible all -m setup
to gather servers facts.

$ ansible all -m apt -a "name=nginx state=present" --sudo
to install the nginx package on debian based systems.

$ ansible all -m service -a "name=mysql state=started" --sudo
to start the service mysqld in Linux systems.

$ ansible all -m win_features -a "name=Web-Server state=present"
to install IIS in Windows systems.

$ ansible all -m win_service -a "name=spooler state=started"
to start the Spooler service in Windows systems.

Add a loop in a Playbook
-------------------------
- tasks:
   - name:  install packages using apt module
     apt: name={{item}} state=installed force=yes
     with_items:
      - package1
      - package2
      - package3

Creating Roles
----------------
to create the role directory structure we use the command:
$ ansible-galaxy init role_name
the you have to add the section roles in your playbook:
roles:
 - role_name1
 - role_name2
 - ....

Asynchronous actions
---------------------
We use the following directves
async: to specify how long to run the task in seconds.
poll: how frequent to check the task, the default is 10s.
to execute two tasks simultaniously we putt poll:0.
