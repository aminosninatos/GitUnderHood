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




