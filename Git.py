Git commands
-------------

$ git status
Displays the status of your working directory. 

git add [file]
Add a file to the staging area.

$ git log [-n count]
List commit history of current branch. -n count limits list to last n
commits.

$ git log --oneline --graph --decorate
An overview with reference labels and history graph. One commit
per line.

$ git fetch [remote]
Fetch changes from the remote, but not update tracking branches.

$ git pull [remote]
Fetch changes from the remote and merge current branch with its
upstream.

$ git diff
Show unstaged changes between your index and
working directory.

$ git push [--tags] [remote]
Push local changes to the remote. Use --tags to push tags.

$ git commit -m 
Commit the staged snapshot, but instead of launching
a text editor, use <message> as the commit message.