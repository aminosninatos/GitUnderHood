Git under the hood
-----------------------

Git gc
------------------------------------------------------------------------------------------
> git gc
garbage collect, cleanup unnecessary files and compressing objects to create .pack files.


Verify a pack
-----------------------------------------------------
> git verify-pack -v filename.pack
to get just the first filed :
> git verify-pack -v filename.pack | awk '{print $1}'


Unpack a file
-----------------------------------------------------
> git unpack-objects filename.pack
you must unpack the file outside the .git directory.


Count number of git commands
--------------------------------
> ls /usr/lib/git-core | wc -l


Short-cut to the first argument of last command
-------------------------------------------------
> mkdir stuff
> cd $_
this will cd to the stuff directory.


Adding a directory to your path
---------------------------------
> PATH+=:directory-path
for example  > PATH+=:~/bin
to verify  > echo $PATH


Create a 10 lines README file
------------------------------------------------------------------------
> for i in {1..10}; do echo this is line $i; done > README; cat README


Count how many characters in a string
------------------------------------------------------------------------------------------
to see how many characters:
> echo e5e776e88e6a77ab737dbb77ddeee6625  | wc -c
To display the file in character format, use the -c option:
> echo e5e776e88e6a77ab737dbb77ddeee6625  | od -c
The od (stands for octal dump) command displays a file in octal (base 8) format by default.


Compare two directories with its subdirectories
-------------------------------------------------
> diff -r dir1 dir2


Generate a public keys pairs
-------------------------------------
> ssh-keygen
> cd .ssh
> cat id_rsa.pub >> authorized_keys


Size of a directory
-------------------------------------------------
> du -sh dir
to get rid of empty directories
> find dir -type d -empty | xargs rmdir
to show  broken symlinks
> find dir -type l -xtype l

Time a command
---------------------------------------------------------
in linux to see how much time a command take to execute
> time command


Packages count
----------------------------------
> apt-get cache search . | wc -l


Pushd, popd & cd commands
----------------------------------------------------------------------------
> pushd dir : move to dir but save in the stack the directory you came from.
> popd  : move back to the saved directory.
> cd -  : move to the last directory you were in.

Counting the source lines of code in a directory
--------------------------------------------------
> sloccount dir 

Showing refs
---------------
> git show-ref

Git files
-----------------------------------------------------------------------
> git cat-file -t  filename or hash
to get the type of  the object : blob(data), tree, commit & tag.
> git cat-file -p  filename or hash
to print it. 


Sed command
-------------------------------------------------------------------------------------
> sed 's/string1/string2/g' filename
to  change any occurence of the string1 to string2 even if string1 is part of word
s: substitute   g: global

> sed 's/\bstring1\b/string2/g' filename
to  change the exact match only of the string1 to string2
b: boundaries

> sed 's/^string1/string2/g' filename
to  change any line that begins with string1 to string2
^: beginning of the line

> sed 's/string1$/string2/g' filename
to  change any line that ends with string1 to string2
$: end of the line

> sed 's/[0-9]/(&)/g' filename
to  change any numeric to (numeric)
[0-9]: all numerical characters &: matched string

> sed '/string/d' filename
delete any line that contains part of whole string

> sed -i '/string/d' filename
-i: if you want to change modifications directly to the file


Staged files or Index or cache
-----------------------------------------------------
> git ls-files --stage
to see what is in the index = staging area = cache


AWK command line
---------------------------------------------------------------------------------------------------------------------------------------------
The basic format of an awk command looks like this:
> awk 'pattern {action}' input-file > output-file

Awk assigns some variables for each data field found:
$0 for the whole line.
$1 for the first field.
$2 for the second field.
$n for the nth field.
> awk '{print $1}' myfile    : displays the first field
you can specify the separator using -F option:
> awk -F: '{print $1}' /etc/passwd    in this case separator = ":"

To run multiple commands, separate them with a semicolon like this:
> echo "Hello Tom" | awk '{$2="Adam"; print $0}'   this displays "Hello Adam"

If you need to create a title & a footer for your result:
> awk 'BEGIN {print "The File Contents:"}; {print $0}; END {print "File footer"}' myfile

> awk '/string/' filename
to get all the lines that contain the occurence of string

> awk '/^[0-9]/' filename
to get all the lines that start with a number

> awk '{if ($1 ~ /[1-3]/) print }' filename
if the first column contains 1 or 2 or 3 print the line

> awk '$7=="7.30" { print $3 }' input-file
The list of statements inside the curly brackets ('{','}') is called a block. 
If you put a conditional expression in front of a block, the statement inside the block will be 
executed  only if the condition is true

> awk 'match($7,/tux/" { print $3 }' input-file
if column 7 matches the word tux print column 3

> awk 'BEGIN { print "Log access to webserver" } {ip[$1]++} END{ for (i in ip) print i, "acceed: ", ip[i] , " times" }' input-file
this will print how many times an ip address in column 1 has accessed the webserver


Create two file  using {}
------------------------------------------------------------------------------
> touch ignored-by-{gitignore,exclude}
this will create 2 files :  ignored-by-gitignore &  ignored-by-exclude


.Git directory structure
--------------------------------------------------------------------------------------------------------------
COMMIT_EDITMSG : last commit message
config : local configuration information
description : it s used by other programs its just a comment
HEAD : the last thing that you check up
/hooks : programs you run automatically when you execute some commands, you have to remove .sample
index : the stageing area
info/exclude : patterns that git ignores
logs/ : keeps history
refs/ : sha1 simple names for sha1 or ascii file 

Characters count
--------------------------------------------------------------------------------------
> echo hash  | wc -c
if you use echo then it will add another character which is the new line character.


Octal dump
----------------------------------------------------------------
> od filename
to dump a file in octal format.
> od -c filename
to dump a file in  character format.
> od -x filename
to dump a file in hexadecimal format.
> od  -xc filename
to dump a file in hexadecimal & character format.


Head command
----------------------------------------------------
> head filename
by default it returns the first 10 lines of a file.
> head -n 5 filename
prints the fisrt 5 lines.
> head -c 20 filename
prints the first 20 bytes.


Tail command
------------------------------------------------------------------
like the head command but it prints the last 10 lines by default.
you can use it with the same options as head command.
> tail -f filename
in order to monitor changes of a file in real time.


Inode
------------------------------------------------------------
> ls -i filename
shows the inode number of a file or directory.
> ln file1 file2
both files will have the same inode number.
> ls -d  directory
shows directory entries instead of contents.


Remove command
-------------------------------------------------------------------------
by default rm only removes files not directories
> rm -r
to remove a directory recursevly including its contents.
> rm -f file
force to remove a file or directory without prompting for confirmation.
> rm -rv directory
to show information while deleting.


Clone a repo locally
------------------------------------------
> git clone --bare  path_repo_name
creates a repo locally called bare repo.


Xargs command
---------------------------------------------------------------------------
it takes output of a command and passes it as argument of another command
> echo 'one two three' | xargs mkdir
will create 3 directories one, two and three.
The most common usage of xargs is to use it with the find command:
> find /tmp -mtime +14 | xargs rm


Find command
---------------------------------------------------------------------------------------------------
find [where to start searching from] [expression determines what to find] [-options] [what to find].
> find . -name filename
searches the current directory for a file with a specific name.
> find . -empty
searches the current directory for empty files and folders.
> find / -name .DS_Store -delete
is equivalent to : > find / -name ".DS_Store"  -exec rm {} \;
> find / -type f
displays only filenames in the / directory


Create multiple directories
----------------------------------------------------
> for i in dir1 dir2 dir3; do mkdir $i; done


Echo command
--------------------------------------------------------------------------------
> echo "something" >> file
will append something to the end of the file.
> echo "something" > file
everything already present in the file would have been replaced by something. 


Copy command
-------------------------------------------------------------------------------------
> cp -a dir1 dir2
-a means 3 things:
1.preserve timestamps, permissions, group, user (if you re running as root).
2.preserves symbolic links (no dereference).
3.recursive copy.


Bash script
--------------------------------------------------------------------------------------------------------------------------------------
>#/bin/bash -eu

the -e option means "if any pipeline ever ends with a non-zero ('error') exit status, terminate the script immediately".
the -u option means warn for typos in bash variables.
>dir=${1:sctarch}
sets the variable dir  to be either something giving in the command line or by default the string "scratch".
>[[ -d $dir]]  &&  rm -rf $dir
[[ is bash s improvement to the [ it lets you use && and || operators to test booleans.
-d to test if a directory exists.
"&&" lets you do something based on whether the previous command completed successfully.


Shopt
-----------------------------------------------------------------------------------------------------------------------------------------
is a shell builtin command to set and unset (remove) various Bash shell options.
-s :  to set or enable the option
-u : yo unset or disable the option
> shopt -s globstar
the pattern ‘**’ used in a filename expansion context will match a files and zero or more directories and subdirectories. 
If the pattern is followed by a ‘/’, only directories and subdirectories match.


File command
--------------------------------------------------
>file filename
lets you determine the actual file type.


Git hash-object
-------------------------------------------
> git hash-object object_name
to get the SHA-1 hash of files.


.Gitkeep
------------------------------------------------------------------------------------------------------
to allow en empty directory to be tracked by git you must add .gitkeep file to this empty directory.


Find empty directories
--------------------------------------------------------------------------------
> find . -type d -empty | fgrep -v .git
fgrep is equivlent to grep -F  searches a file using a fixed pattern.
fgrep -v  to select not matching .git directory.


Here document
----------------------------------------------------------------------------------------------------------------
> cat << EOF > filename
'EOF' is the limiting string, anything entered to the stdin will be writing to the file until the word 'EOF'.







