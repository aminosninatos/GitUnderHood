Linux under the hood


Loaded libs
-----------------------------------------------------
# ldd program_file
to see the libraries that the program calls

User space vs Kernel space
----------------------------------------------------------------------------------------
hardware access in restricted only to the kernel
kernel provides system calls for users and processes to access hardware
user space is memory that is allocated by the kernel for user processes

Strace & Ltrace
-----------------------------------------------------------------------------------
> strace command
to see what is really happening behind the scenes(system calls)
> ltrace command
shows library calls

Signals
-----------------------------------------------------------------------------------------------------
provides a software interrupt its a method to tell a process that it has to do something

