Turn paged output
--------------------------
for git branch :
git config --global pager.branch false
for git log :
git config --global pager.log false

Status in silent mode
-------------------------------------------------------------------
git status -s
will show a brief summary about the status of the files instead of long messages

Renaming & removing files
-----------------------------
git mv old_file new_file
git rm filename
then you have to commit

Create a branch and switch to it the delete it
-----------------------------------------------------
git checkout -b branch_name
git branch -d branch_name

See unstages & staged changes
-----------------------------------------
git diff                     shows only unstaged changes
git diff --staged    shows only staged changes
git diff  HEAD    shows  unstaged &  staged changes

Explore  objects content
----------------------------------
git cat-file -p SHA1-hash

git show
----------------------------------------------------------------------------------------
is equivalent to git show HEAD, i.e. the latest commit in the current branch

Creating a tag
--------------------------------------------------------------------------
whenever you push something to production you have to tag it:
git tag v1.0.0
the it will be  visible when you execute git log or git show v1.0.0



Cancel changes
------------------------
git reset --soft HEAD^   undo last commit, put changes into staging
git commit --amend -m "New message"    change the last commit
git reset --hard HEAD^    undo last commit and all changes
git reset --hard HEAD^^   undo last 2 commits and all chnages

See changes in a commit
---------------------------------------
git show  git show 9e2546
or if you want to have a summary :
git show --shortstat 9e2546

Checkout
-----------------------
git checkout filename
to cancel the last changes & modification made to the file

Diff
--------
git diff --color-words
or
gif diff --word-diff
to get differences of small changes like words

Fetch
-------------------------------------------
git fetch 
only downloads new data from a remote repository - but it does not integrate any of this new data into your working file.

Show non-pushed commits
---------------------------------
git log origin/master..HEAD


Show non-pulled commits
-------------------------------
git fetch origin master
then :
git diff master origin/master


Set your details
---------------------------------------------------------------
git config --global user.name "John Doe"
git config --global user.email "john@example.com"


See your settings
---------------------
git config --list

Carriage return & line feed settings
--------------------------------------------------
in windows you should use :
git config --global core.autocrlf true
in linux or mac you should use :
git config --global core.autocrlf  input

Alias
---------------
create .gitconfig file to your home directory then add
[alias]
alias_name = log --oneline
then you can  use the alias as follow
git alias_name


Go back to a specific commit then go back to the present
-------------------------------------------------------------------
git checkout a1b2c3
... and return to master with:
git checkout master


See the files that changed between two commits
---------------------------------------------------------
git diff --name-only COMMIT1_ID COMMIT2_ID

Change message of last commit
----------------------------------------
git commit --amend -m "New commit message"


Push local commits to remote branch
---------------------------------------------
git push origin master


See commit history printed in single lines
------------------------------------------------
git log --pretty=oneline
or
git log --online


Commits in a specified date range
---------------------------------------------
git log --since '2018-12-10 00:00:00'
git log --until '2018-12-10 00:00:00'
git log --after '2018-12-10 00:00:00'
git log --before '2018-12-10 00:00:00'


Remove files from staging area
----------------------------------------
git rm --cached filename
or 
git reset filename


Add modified files to the staging area and commit them
-----------------------------------------------------------------
git commit -a -m "Do something once more"

Typical git workflow
-----------------------------------------------------------------
1- create a new branch 
git branch new-branch
2- switch to that branch
git checkout new-branch
3- do all the modification in your project
4- add your files to staging area and commit them
git add -A
git commit -m "your comments"
5- push to a remore repository
git push -u origin new-branch
6- if everything is ok in the new branch
git checkout master
git  merge new-branch
git push origin master
7- delete the new-branch form local & remote
git branch -d new-branch
git push origin --delete new-branch


See the files that changed in commits
----------------------------------------------
git log --stat

Create a tag view it and push it to remote repository
--------------------------------------------------------------
git tag tag_name
git tag
git push --tags

Password prompt whenever pushing or pulling
--------------------------------------------------------
git config --system --unset credential.helper
git config --global --unset credential.helper
git config --local --unset credential.helper















