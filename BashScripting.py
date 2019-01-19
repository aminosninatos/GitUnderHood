Bash scripting
-------------------


Shebang
------------------------------------------------------------------
#!/bin/bash
tells which interpreter is going to be used to execute the script.
here '#' is not a comment in this case.

Exit status
-------------------------------------------
> echo $? 
to get the exit status of the last command.

Path variable
-------------------------------------------------------------------------
on linux the current directory is not in the $PATH so to execute a script:
> ./myscript


2>&1  expression
---------------------------------------------------------------------------------
"strace" prints its traces on standard error, not on standard output. 
thats because its common to want to redirect the standard output of the program.
but usually not a problem that strace stderr and the programs stderr are mixed.
so you should redirect strace stderr to stdout to be able to pipe it:
> sudo strace -p $(pgrep apache2) 2>&1 | grep open

Bash -x
-----------------------------------------------------------------
> bash -x script
if you want your script to show every line before executing it.

Variable Shell and SubShell
-----------------------------------------------------------------------------------------------------
a subshell is created whenever you execute a script.
a variable is only effective in the shell when it was defined.
we use "EXPORT" to make it also available in subshells.
/etc/profile is processed when OPENING a LOGIN SHELL - user specific version is on ~/.bash_profile.
/etc/bashrc is processed when OPENING a SUBSHELL - user specific version is on ~/.bashrc.

Sourcing
---------------------------------------------------------------------
the content of one script can be included in another script.
we use the "source" command or the "." command to source a script.

Arguments
----------------------------------------------------------------
"$0" refers to the name of the script itself.
"$1" "$2" $... refer to the first second .... argument.
"$@" refers to all arguments provided one by one.
"$#" refers to the count of arguments.
"$*" refers to a single string that contains all arguments.

Command substitution
-----------------------------------------------------------------------
allows using the result of a command in a script by using the "$" sign.
> ls -l $(which passwd)

substitution operator
--------------------------------------------------------------------------------------
${VAR:-word} if $var exists, use its value if not display the value "word".
${VAR:=word} if $var exists, use its value if not set the default value to "word".
${VAR:?message} if $var exists, use its value if not display var followed by a message.

Pattern matching
-----------------------------------------------------------------------------------------------------------------
is used to remove patterns from a variable.
"${VAR#pattern}" search the pattern of the variable value & delete the shortest part that matches.
"${VAR##pattern}" search the pattern of the variable value & delete the longest part that matches.
"${VAR%pattern}" if the pattern matches the end of the variable value then delete the shortest part that matches.
"${VAR%%pattern}" if the pattern matches the end of the variable value then delete the longest part that matches.






