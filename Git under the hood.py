Git under the hood
-----------------------

Verify a pack
-----------------------------------------------------
> git verify-pack -v filename.pack
to get just the first filed :
> git verify-pack -v filename.pack | awk '{print $1}'


Unpack a file
-----------------------------------------------------
> git unpack-objects filename.pack
you must unpack the file outside the .git directory


Count command in git
---------------------------------
> ls /usr/lib/git-core | wc -l


Short-cut to the first argument
-----------------------------------------
> mkdir stuff
> cd $_
this will cd to the stuff directory.


Adding a directory to your path
---------------------------------------------
> PATH+=:directory-path
for example  > PATH+=:~/bin
to verify  > echo $PATH


Create a 10 lines README file
---------------------------------------------------------------------------------
> for i in {1..10}; do echo this is line $i; done > README; cat README


Count how many characters in a string
------------------------------------------------------
to see how many characters:
> echo e5e776e88e6a77ab737dbb77ddeee6625  | wc -c
To display the file in character format, use the -c option:
> echo e5e776e88e6a77ab737dbb77ddeee6625  | od -c
The od (stands for octal dump) command displays a file in octal (base 8) format by default.


Compare two directories with its subdirectories
-------------------------------------------------------------
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
-------------------------------------------------------
in linux to see how much time a command take
> time command


Packages count
---------------------------------------
> apt-get cache search . | wc -l


Pushd, popd & cd commands
-----------------------------------------------------------------------------------
> pushd dir : move to dir but save in the stack the directory i came from
> popd  : move back to the saved directory
> cd -  : move to the last directory you were in

Counting the source lines of code in a directory
--------------------------------------------------------------
> sloccount dir 

Showing refs
-----------------------
> git show-ref

Git files
-----------------------------------------------------------------------
> git cat-file -t  filename or hash
to get the type of  the object : blob(data), tree, commit & tag
> git cat-file -p  filename or hash
to print it 


Sed command
---------------------------------------------------------------------------------------------
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
-------------------------------------------------------------
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
------------------------------------------------------------------------------------------------
> echo hash  | wc -c
if you use echo then it will add another character which is the new line character


Octal dump
----------------------------------------------------------------
> od filename
to dump a file in octal format
> od -c filename
to dump a file in  character format
> od -x filename
to dump a file in hexadecimal format
> od  -xc filename
to dump a file in hexadecimal & character format


Head command
----------------------------------------------------
> head filename
by default it returns the first 10 lines of a file
> head -n 5 filename
prints the fisrt 5 lines
> head -c 20 filename
prints the first 20 bytes











