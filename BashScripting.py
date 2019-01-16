Bash scripting
-------------------


Shebang
-------------------------------------------------------------
#!/bin/bash
the nterpreter that is going to be used to execute the script
here '#' is not a comment in this case

Exit status
-------------------------------------------
# echo $? 
to get the exit status of the last command

Path variable
-------------------------------------------------------------------------
on linux the current directory is not in the $PATH so to execute a script
# ./myscript


2>&1  expression
---------------------------------------------------------------------------------
strace prints its traces on standard error, not on standard output. 
thats because its common to want to redirect the standard output of the program.
but usually not a problem that strace stderr and the programs stderr are mixed.
so you should redirect strace stderr to stdout to be able to pipe it:
# sudo strace -p $(pgrep apache2) 2>&1 | grep open

