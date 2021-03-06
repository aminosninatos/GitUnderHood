Linux under the hood
------------------------

Loaded libs
---------------------------------------------
> ldd program_file
to see the libraries that the program calls.

User space vs Kernel space
-------------------------------------------------------------------------
hardware access is restricted only to the kernel.
kernel provides system calls for users & processes to access hardware.
user space is memory that is allocated by the kernel for user processes.

Strace & Ltrace
----------------------------------------------------------------
> strace command
to see what is really happening behind the scenes(system calls).
> ltrace command
shows library calls.

Signals
-----------------------------------------------------------------------------------------
provides a software interrupt its a method to tell a process that it has to do something.

Master Boot Record
--------------------------------------------------------------------------------------
> xxd -l 512 /dev/sda
to see the fisrt 512 bytes of the disk, we use the xxd which is a hexadecimal viewer.
55aa is the magic code which couclude the mbr.

Bios & UEFI
-------------------------------------------------------------------------------------------------
on BIOS system, MBR is read from disk & the stage 1 boot loader is activated.
on UEFI system, GPT partition table is used which contains EFI system partition which contains a 
directory named efi.

Initramfs
----------------------------------------------------------------------------------------------------
it is a initial filesystems that has been compiled to contains the root filesystem and some drivers.

Init & systemd
-----------------------------------------------------------
init is the first process that the kernel has to look for.
in newer linux distro init is redirected to systemd.

Logging
-----------------------------------------------------------
applications may direct the logging to:
stderr.
own log (like apache).
rsyslog (centralize solution).
systemd-journald (using the command journalctl).

Unit files
-------------------------------------------------------------------------------
systemd unit files define what needs to be started like:
service - Mount - Timer - Path - target...
there are stored in /usr/lib/systemd/sytem &  /etc/systemd/system

Systemd target
--------------------------------
a target is a group of units.

Comparing MBR & GPT
------------------------------------------------------
MBR partitions:
space for 4 partitions.
stored in mbr (512bytes).
uses primary, extended & logical partitions.
maximum addressable disk size is 2 TB.
GPT partitions:
space for 128 partitions.
stored in GPT partition.
no more primary, extended & logical partitions.
default on UEFI systems.
stores backup at the end of the disk.
commands used to deals with them
for GPT  > gdisk /dev/sdx
for MBR > fdisk /dev/sdx

Device mapper
-----------------------------------------------------------------------------------------------
a generic interface to the linux kernel that can be used by different storage solutions.
lvm, encrypted volumes or md go through device mapper.
in order to deal with it we use the command > dmsetup.

VFS
--------------------------------------------------------------------------------------
is the abstraction layer that can talk to all different filesystems(ext4,btrfs...).

Btrfs
---------------------------------------------------------------------------------------------
is a new filesystem that has new features like 'cow' copy on write and subvolumes.
OpenSuse uses this kind of filesystem.
to deal with it we use  the command > btrfs.
it uses also snapshots that can be managed by the command > snapper.

Inode
-------------------------------------------------------------------------------
a file is a bunch of block, an inode is the total administration of the file.
we use the command > debugfs to see the contents of an inode.
you should always use it after shutting down the filesystem.

FUSE
------------------------------------------------------------------------------------------------------
is a component part of the VFS, it allows more flexible system usage.
for example ZFS  & NTFS are not compatible with the linux kernel so it's handled by FUSE.

iSCSI
------------------------------------------------------
is storage over the network."i" for ip (network).
> targetcli  is the utility use to configure it.

Page cache or cache
-----------------------------------------------------------------------------------------------------------
is RAM that is not used to store application data and is available and can be easily cleared.
> echo 3 >  /proc/sys/vm/drop_caches
is the command used to free cache then we can verify using > free -m or  > less /proc/meminfo

Swap memory
------------------------------------------------------------------------------------------------------
the best type  to know how much swap you use is to monitor inative ananymous memory :
inactive anon = swap

Fork() & exec()
---------------------------------------------------------------------------------------
fork() is a system call where process makes a copy of itself to create a child process.
next the child process calls the exec() system call to overlay itself with  other program.
exec() can be used as an alterative to fork(), in exec() the parent code is replaced with  the child  code
and the parent ceases to exist.

Taskset
-----------------------------------------------
to pin a specific process to a specific processor:
> taskset -pc 3 $(pidof dd)
pin the process 'dd' to processor 3

Top command
--------------------------------------------------------------------------
to add specific column to the displyed columns we use the 'f' key
after you select the desired column to make changes permanent press capital 'W'

Zombie process
------------------------------------------------------------------
is a leftover bit of dead processes that hasnt been cleaned up properly.

Chrt
------------------------------------------
manipulate real-time attributes of a process.

Socket
-----------------------------------------------------------------------
is a component that allows communication between processes.
is created as a file system inode which allows two processses to communicate.

D-bus
---------------------------------------------------------------------------------------------
provides a software abstraction that creates on a virtual channel than can be used for  communication
between a group of processes.

Monitoring processes
------------------------------------------------------------------------------------
in order to do that we explore the /proc directory and we dive into the pid process directory.

DAC (Discretionary Access Control)
-------------------------------------------------------------------------------------------------------
is a means of restrictions access to objects based on the identity of subjects and/or groups to which they belong.
in Linux two machanisms for that : owner based permissions & system capabilities.

MAC (Mandatory Access Control)
--------------------------------
SELinux : developped by Redhat.
Apparmor : used in Ubuntu & Suse.
Smack : a simplified MAC solutions.

Kernel device interface
-------------------------------------------------------------------------
hardware <----> driver(kernel modules)<----> /sys <------> kernel.
udev is the process that helps kernel initializing hardware.
/dev (device nodes)<----> major & minor <----> kernel <---->  /sys (sysfs).
device nodes are  files that interface the user & allow the user to use hardware.

Monitoring hardware
----------------------------------------------------
> dmidecode | less  : showing BIOS information.
> lspci -k  : shows pci interfaces & kernel modules.
> lsusb  : shows usb interfaces.
> dmesg | less 
> lsscsi
> lsblk
> lscpu
> lsdev

Sysfs
----------------------------------------------------------------------
is used by the kernel to provide information about devices & hardware.
> udevadm   is a command to interface query device info.

Udev
-------------------------------------------------------------------------------
the kernel initiates device loading and next sends out uevents to udevd daemon.
udevd catches the event and decides how to handle it.
udevd next reads its rules(/lib/udev/rules.d) and takes actions. 
> udevadm monitor  : is udev monitoring tool.

Kernel modules
------------------------------------------------------
> lsmod : to list all loaded modules.
> modinfo module_name  : to get info about a module.
> modprobe module_name  : to load a module.
> modprobe -r module_name  : to remove a module.

Tainted kernel
-----------------------------------------------------------------------
means your kernel is using no open source modules(propriatary drivers).
> cat /proc/sys/kernel/Tainted
is 0 then you are using only open source modules else you are tainted .

Proc filesystem
------------------------------------------------------------------------------
is devided in 3 main areas:
-files.
-pid.
-sys which has subdirectories like kernel, net(networking) and vm(memory).
you can make changes using > echo value command but that will be only runtime.
if you want changes to become permanent after reboot you should use > sysctl.
sysctl command reads the /etc/sysctl.conf file.
> sysctl -a will show you the tuneables variables.

Ip command
--------------------------------------------------------------------
IFCONFIG command is deprecated and replaced by IP command in Linux. 
> ip addr add 192.168.50.5 dev eth1
to assign IP Address to a specific interface (eth1).
> ip addr show or > ip a
To get the depth information of your network interfaces.

SSH keys
------------------------------------------------------------------------------
to set up ssh keys so a workstation can login to ubuntu without credentials:
on the workstation:
> ssh-keygen : generates a public key pair.
> ssh-copy-id ubuntu : copy the public key over the ubuntu server.
> ssh ubuntu : now you can login without providing a password.

Memory optimization
---------------------------------------------------------
to set the maximium limit memory for an application:
> systemctl set-property httpd.service MemoryLimit=512M
> systemctl daemon-reload
> systemctl restart httpd
> systemctl status httpd

I/O optimization
-------------------------------
to see if a file is fragmented:
> filefrag -v file_name

Configuring LVM storage 
---------------------------------------------------------------------
1- manual install.
2- create a  new primary partition  : /boot partition (around 250 MB).
3- use  configure logical volume manager.
4- create a volume groupe by using teh free remaining space.
5- create a logical volume on this volume groupe lvsystem.
6- create a logical volume on this volume groupe lvswap.
7- create a logical volume on this volume groupe lvsrv.
8- use the corresponding filesystem & mount point to each logical volume.
9- write changes to disk.










