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
12. Install vim editor.
13. Install youtube-dl to download youtube videos.   


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
in order to use smartctl you must install smartmontools package.

CHECK INTERFACE TRAFFIC
------------------------
install nload package then run : > nload

CHECK HDD TEMP
------------------------
install hddtemp package then run : > hddtemp /dev/sdx

CHECK CPU MEM SERVICES
------------------------
install htop package then run : > htop 

YUM COMMANDS 
--------------
> yum repolist
> yum history
> yum history info id_num
> yum history undo id_num
> cat /var/log/yum.log 
> cat /etc/yum.repo.d/xxx.repo 


CHECK DISK PARTITION
------------------------
> lsblk

CHECK LVM
------------------------
> pvdisplay
> vgdisplay
> lvdisplay 

CHECK SERVICES USING SYSTEMD 
---------------------------------------------------------
> systemctl --state=running : check running services
> systemctl status servcice_name : check a service status 
> systemctl start servcice_name : start a service
> systemctl enable servcice_name : start a service at boot
> systemctl restart servcice_name : stop & start a service
> systemctl --failed : check failed services 

SHUTDOWN THE SYSTEM
--------------------
> systemctl poweroff : to shutdown the system
> systemctl reboot : to reboot the system
> systemctl suspend  : to suspend the system

TRANSMISSION TORRENT CLIENT
----------------------------
> transmission-daemon   : to start working with it.
> transmission-daemon --download-dir   : location of downloads.
transmission-daemon --dump-settings  : to view the configguration.

> transmission-remote -a 'magnet-link'  : to add a torrent file.
> transmission-remote -l : to view status of downloads.
> transmission-remote -t id-torrent --remove : to remove a torrent.
> transmission-remote -t id-torrent --info : to view info of a torrent.
> transmission-remote -t id-torrent --files : to view all files of a torrent.
> transmission-remote -t id-torrent --stop : to stop a torrent.
> transmission-remote -t id-torrent --start : to start a torrent.








