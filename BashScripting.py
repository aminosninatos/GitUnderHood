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

Grep
--------------------------------------------------------
> grep -v  exclude lines that match the pattern.
> grep -r  recursive that searches also subdirectories.

3 ways to test
-------------------------------------------------------------
test -z $1  old method, using internal bash command.
[-z $1]     equivalent to test.
[[-z $1]]   new improved version that has "||" "&&" build in.  

Using "&&" and "||"
---------------------------------------------------------------------------------------------------------------------
"&&" and "||" are the logical AND and OR.
when using "&&" the second command is only executed when the first expression retuns exit code 0(successful).
when using "||" the second command is only executed when the first expression does not return exit 0(Not successful).

Using case
----------------------------------------------
case is used if specific values are expected
case $VAR in
	var1)
    command1;;
    var2)
    command2;;
    *)
    command3;;
 esac

Array
----------------------------------------------------------
an array is a string variable that holds multiple values.
array_name=(x1 x2 x3)
echo ${array_name[0]} first value of the array.
echo ${array_name[@]}  all array values.
echo '${#array_name[@]}' number of array values.

Test command
------------------------------------------------------------
if you want see what does any argument mean in a [-z $VAR] 
you can look at "man test" command.


Menu interface
----------------------------------------------
the select statment is used to create a menu.   
select VAR in X1 X2 X3
notice the use of break in select.

Trap
------------------------------------------------------------
is used to redefine a signal for example to disallow Ctrl+C.


Declaring variables
---------------------------------------
is not required but can be useful.
declare -r var (readonly)
declare -i var (number)
declare -a var (array)
declare -f function_name (function)
declare -x var (export)


list all files
-------------------------------------------
for i in *;do echo $i;done
* means all files in the current directory.


Advanced sed
----------------------------------------------------------------------
to replace /usr/local/bin/old with /common/bin/new can be done using:
sed 's/\/usr\/local\/bin/\/common\/bin/' <old> new
sed 's_/usr/local/bin_/common/bin_' <old> new
sed 's:/usr/local/bin:/common/bin:' <old> new
sed 's|/usr/local/bin|/common/bin|' <old> new


Type command
------------------------------------------------------------------------------
is used to find out what a commmand exactly is : external or internal
internal commands are part of the shell and already in memory
external commands need to be loaded and create a new process when executed
for example 'ls' is external command and its internal equivalent is 'echo *'

Useless commands
--------------------------------------------------------------------------------------
instead of: cat /etc/passwd | grep blah use:  grep blah /etc/passwd
instead of: grep blah myfile | awk '{print $1}' use: awk '/blah/ print{$1}' myfile 


To compare a script performance
----------------------------------
> time my_script
> strace -c my_script


