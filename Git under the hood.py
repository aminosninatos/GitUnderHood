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


