Basic info
------------
> ps auZ – List processes including SELinux context
> ls -Z – List files including SELinux context

> getenforce – Get current mode of SELinux
> sestatus – SELinux status tool

Runtime configuration
----------------------
> setenforce [1|0] – Enable/Disable SELinux (temporary until reboot)

Permanent configuration
------------------------
/etc/selinux/config – Permanent SELinux configuration

SELinux Booleans
----------------
> getsebool -a – Get all SELinux booleans and their values
> semanage boolean --list – List all SELinux booleans, their current and default values and short description.
> setsebool httpd_enable_cgi on – Enable a SELinux boolean (temporary until reboot)
> setsebool -P httpd_enable_cgi on – Enable a SELinux boolean (persistently)

File context
--------------
semanage fcontext -l – List file context mapping definitions used by restorecon
semanage fcontext -a -t httpd_sys_content_t "/webpages(/.*)?" – Add a new definition

Port labeling
--------------
semanage port -l – List current port label assignments
semanage port -a -t http_port_t -p tcp 81 – Allow httpd service to listen on port 81/TCP
semanage port -d -t http_port_t -p tcp 81 – Remove a custom port labeling

File context (labeling)
------------------------
restorecon -vR /foo/bar – Restore file(s) default SELinux context
chcon -R /foo/bar – Change SELinux context (temporary until next run of restorecon on the file/dir)

Relabeling whole file system
------------------------------
Create /.autorelabel file and reboot.

Log files
-----------
/var/log/audit/audit.log – Used by default if auditd daemon is running
/var/log/messages – Used when auditd is not running or when setroubleshoot-server is installed.