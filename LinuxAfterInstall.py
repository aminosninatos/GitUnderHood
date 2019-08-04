Linux After Install
----------------------------------------------------
----------------------------------------------------
RHEL
-----------------------------------------------------------------------------------
1.Enable rhel repos using commands:
> subscription-manager repos --enable=rhel-7-server-rpms
> subscription-manager repos --enable=rhel-7-server-extras-rpms
> subscription-manager repos --enable=rhel-7-server-optional-rpms
	
Applications
----------------------------------------------------------------------------------------------------------------------------------	
2. Install vlc
3. Install simplescreenrecorder
4. Install teamviewer
5. Install private & public keys (run > ssh-keygen command) and put public in authorized_keys/ directory in .ssh/
6. Modify sshd_config file to allow only public key authentication (PasswordAuthetication no)
7. Install docker
8. Install zsh shell & Install Oh-my-zsh & install zsh-autosuggestions plugin in .zshrc file & install tilix terminal
9. Install ddclient & verify using :
> ddclient -daemon=0 -debug -verbose -noquiet -debug -query
10. Customize vim by adding .vimrc & pathogen plugin with vim-airline & Monokai color scheme
11. Configure static IP : vim /etc/sysconfig/network-scripts/ifcfg-eth016 & systemctl stop NetworkManager  


Selinux important commands
------------------------------------------------------------------------------------------
- Open sepcial port : > semanage port -a -t http_port_t -p tcp 8081
- Check that the port is added: > semanage port -l | grep 8081
- Install setroubleshoot packages : > setroubleshoot setools
- Analyzes the audit log used by SELinux : > sealert -a /var/log/audit/audit.log


Journalctl command
------------------------------------------------------------------------
- Filter only errors : > journalctl -p err
- View live logs : > journalctl -f
- View logs to a specific service : > journalctl -u service_name
- View short help : > journalctl --help
- View disk occupation of logs : > journalctl --disk-usage


SMART commands
------------------------------------------------------------------
- Get info about HD : > smartctl -i /dev/sdx
- Get Genaral Health : > smartctl -H /dev/sdx
- Short test can be done : > smartctl -t short /dev/dsx





