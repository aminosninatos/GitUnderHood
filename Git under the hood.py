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
----------------------------------
> mkdir stuff
> cd $_
this will cd to the stuff directory.


Adding a directory to your path
-----------------------------------
> PATH+=:directory-path
for example  > PATH+=:~/bin
to verify  > echo $PATH


Create a 10 lines README file
---------------------------------
> for i in {1..10}; do echo this is line $i; done > README; cat README


Count how many characters in a string
--------------------------------------
to see how many characters:
> echo e5e776e88e6a77ab737dbb77ddeee6625  | wc -c
To display the file in character format, use the -c option:
> echo e5e776e88e6a77ab737dbb77ddeee6625  | od -c
The od (stands for octal dump) command displays a file in octal (base 8) format by default.


Compare two directories with its subdirectories
----------------------------------------------------
> diff -r dir1 dir2


Generate a public keys pairs
-------------------------------------
> ssh-keygen
> cd .ssh
> cat id_rsa.pub >> authorized_keys


Size of a directory
----------------------
> du -sh dir
to get rid of empty directories
> find dir -type d -empty | xargs rmdir
to show  broken symlinks
> find dir -type l -xtype l

Time a command
-------------------------------------------------------
in linux to see how much time a command take
> time command






