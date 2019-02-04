Shell Programming
-----------------------------

Part1
----------
In bash, unlike any other language I know, you program interactively, on the command line. Chances are, you use either vi or emacs as an editor. Me, I use "vi," so Ill use that for my examples. (If you use emacs, just substitute emacs commands.)

On the command-line, put it into vi mode, with set -o vi.  Type a few commands:

date
ls
pwd
who
ping -c 1 google.com

Now, imagine you're on a one-line terminal, editing your history. You're in vi "insert mode," since otherwise all your keystrokes would be commands, right?

Go into command mode: type ESC. Now go up a line, with k . Its vi, just a one line terminal. Go up another.  Go back to the date command and hit ENTER.

Hitting ENTER executes the command that was showing in the one-line window, and puts you back into insert mode. You can now type again.

Next, try this:

First ESC to enter command mode.  Next, use k to go up to the ls command, so its showing in your window.  Youre still in command mode, so instead of pressing ENTER, press A to append to the end of the line, and type " /bin"

Now hit enter.  Aha.

Okay, go back to that line, with k , and move your cursor forward to the "/" with the vi command, f/,  (youre still in command mode!), go back into insert mode, with i and type "/usr" so the line reads

ls /usr/bin

Hit ENTER.

I've been pretty verbose, so that all seems like a lot of work, but if you're fluent in vi, all that is in your firmware. The only change is thinking of the command line as a one-line, editor window, with all your "history" stretching above the line you see.

You dont think, "Okay, now I'll go into command mode. Now Ill go to the slash. Now Ill insert some characters." You just edit naturally.  

If you're an emacs user, you start with set -o emacs, then edit the one-line window with emacs commands, but it's the same idea.

Now, use your one-line editor to go back to your who line and change it to 

who am i

This is how you start. Spend some time playing with the one-line editor, and we can go from there.

Doing this will also make you a more fluent vi user. Its a twofer -- a two-for-the-price-of-one special: using your text editor makes you a more fluent bash programmer. Using bash makes you a more fluent editor user.

Now here's a bonus.  Take a look at man ed  the manual page for the original UNIX line editor, and try it out.  It's still on every POSIX-conforming system.

Some time in the Cretaceous, when I started using computers, there were only line editors, no screen editors -- the only editors were line editors. 

And those were only available if you had access to terminals, instead of punch cards. Ill occasionally say, "When I started programming, we wrote programs by punching holes in little pieces of cardboard."  

Then I think, "Wait. Did that really happen, or did it just dream it? It was so long ago ...."

Ken Thompson wrote UNIX in four weeks, while his wife was away on a months vacation in California: a week for the filesystem, a week for process management, a week for the shell, a week for an editor -- ed. 

All were in PDP-7 assembly language, because there were no widely-available, higher-level languages like C yet.

In the 1970's, Bill Joy, at Berkeley, and Ned Irons, at Yale, invented screen editors. Bill Joy's, vi evolved from ed, and lives on. 

Ned's, which was an independent invention, became the RAND editor, and eventually the default editor on IBM's AIX, ined. Soon after these two, Guy Steel and others wrote EMACS.

In vi, you can still go into line-editor mode (also called "ex") with the command Q


Part 2
-------------
Youve had a chance to try out using your vi skills to navigate your command history. What vi commands are especially useful?

The most useful is simply recalling old commands.

You know that vi lets you search a file with the command / . 

You can search through your history with the same command. 

Here, Ill just confess, my mental model breaks down just a little, because the h,j,k,l navigation keys all work as though the history of the file is above your window, but the / command searches backwards in history -- up, not down.

I think, logically, the command should be ? , but that doesnt work.

I won't apologize for it because I didn't make this up. Im just reporting -- just a user.

Still, you can search your history for instances of any string or substring, first with / , and then search for other instances of the same pattern with n , just like in vi.  You should start using that a lot, because its a huge win. 

Once you let the vi commands in your fingers take over, its a lot faster than going back in your history a line at a time until you find what youre looking for.

After all, you wouldnt just press arrow keys in vi to move through a file until you found what you wanted, certainly not if you knew a word to look for, would you?

Speaking of arrow keys, they do work.  You might use those in vi, too. Me, I use the h,j,k,l cursor-motion commands because I started using vi with ADM-3A terminals, which actually had their H, J, K, and L keycaps marked with arrow keys. 

That is, Im sure, why Bill Joy used these letters for the vi cursor-motion commands, too.

Some other things in bash command-editing arent completely logical, but also work anyway.

One is ^r (ctrl-r), which also does a search back through your history. Its really an emacs command, but its so useful that you usually find it in vi-mode for bash, too. 

Two things make it more useful than vi's / search. First, because emacs is modeless its commands work even in insert mode -- you don't have to go into command mode to use it.  Thats really handy. 

Second, it's incremental (again, like the emacs command). Type ^r to start it and you'll see a prompt for what to search for.  Type 'f' and it will search for the first 'f' in your history. Next, type 'o' and it will look for the first "fo" -- perhaps a for loop. 

You're really looking for "foo"? Just type the third "o" .  Make sure you don't hit ENTER until youve found what you want.

Also, theres no separate command for "find the next one."  If you find "foo" but its not the "foo" you wanted, just type ^r again, and bash will find you the next "foo".  When you find the command you were looking for, a simple ENTER will re-execute it.

These are so handy that I switched to them right away. I always use ^r to search my history.

Searching is especially useful if you had a command you used three weeks ago, and you sort of remember what it was, but forget some key details. "What were those flags I was using?"  This will only work if your history goes back three weeks.

The bash default settings only keep the last 500 commands. Thats too few for someone with a memory as bad as mine.

In English, people with good memories will tell you, "I have a mind like a steel trap," which means once they hear or learn something, their mind seizes it and holds on to it firmly. I have a mind like a steel colander.

There are a lot of different tricks you can do to make history more useful, by setting various bash variables. You can read about them in the bash man page. Here are three I recommend:

shopt -s histappend
HISTFILESIZE=100000000
HISTSIZE=100000

I think the first one is the bash default. You can find out what your setting is with this:

shopt | grep histappend

The next two just say "Keep a lot of history".  You can check your settings for these with

set | grep HIST

I set them in my .bashrc .

As an historical note, I think the first shell to support history was Bill Joys csh, which used a complicated bang (! is pronounced "bang") syntax to refer to previous commands. 

Csh users could refer to the 69th command in the history file as !69.  !-5 meant "five commands before this one" . 

There were more.  Bash supports many of these, to help old csh users convert to bash more easily, but most people who start with bash dont ever learn or use them; directly editing your history with vi-commands feels more natural.

The bang-command remnant I sometimes see, when I watch folks use bash, is !! , which means "the previous command."  I don't find this any easier than ESC-k, or up-arrow, but that's where it comes from.

Having an actual editor to edit command-line history was the brainchild of Dave Korn, who put it into his Korn shell.  I'd guess it was Chet Ramey, who's been the bash maintainer for decades, who put it into bash. 

Im sure as soon as Chet saw it, he thought, "Wow! Why didnt anyone do that before?" Both Dave and Chet were very active in crafting the POSIX shell spec, so its also a POSIX requirement.

Chet is also the GNU readline maintainer, which you can link into your own command-line apps to provide command-line editing.

When you run a command that gives you prompts and lets you edit what you type, chances are you its using GNU readline, and you can use all your favorite editor commands. You can find out more about readline by looking in Wikipedia and by asking your friend, Google.

Part 3
-----------
Another piece of command-line programming that isnt quite "in-model" is # .

Try this: At a prompt (that is, in "insert mode"), type this command, but do not press ENTER:

for i in {0..7}; do echo $i; done

Now, instead of ENTER, press ESC to switch to command mode. You should still be at the end of the line. The cursor will move back to the 'e' at the end of done

Next, type a pound (hash, octothorpe, or whatever you call it): #

Bash sticks a "#" symbol at the beginning of the line! Press ENTER and you get a new prompt, but nothing else happens; you turned your for loop into a comment.

The pound command, in vi-command-mode, instantly turns the line into a comment.  Pressing ENTER puts that commented line into your command history.

Try this: Recall your last command (how you do this should now be in your firmware).  Its that comment.

Delete the pound sign (x) and press ENTER. See how the loop executes?

When could you use this? Heres a simple use case:

You're typing a command, and suddenly realize you can't finish typing it correctly without stopping to check something or look something up.

Comment out the line, go look up what you need, recall the line, use vi commands to edit it, then remove the comment symbol and execute it.

Another is if youre typing a long command that does something important, like renaming a lot of files. 

Making it a comment lets you complete your typing, then recall it, look through it at leisure, copy-edit it if you find a typo, perhaps even test snippets, and then finally execute it when youre convinced its what you want.

It lets you encourage yourself to try more complex programming on the command line without getting nervous.

I do this all the time.  Really. Its super-useful.  You should use it every day until it becomes natural.Bash makes it easy to turn commands into comments. Shell comments go into your history.

Editing your history lets you turn comments back into commands.

Books about shell programming might tell you to put comments into scripts. Im saying "Use comments in interactive programming!" Bash agrees and goes out of its way to make that easy.

The shell didnt always have comments.

From earliest times, UNIX systems made : and true synonyms by linking /bin/true to /bin/:

Why? Before programmers could comment scripts like this:

# here is the beginning of the script
date
# and here is the end of the script

they commented them like this: 

: here is the beginning of the script
date
: and here is the end of the script

You commented your scripts by using the command  true , which always succeeds and ignores its arguments.  You still can.

But wait. How are these different? Do you even need comments? Is a comment different from a command that does nothing?

Yes, it is. This does what you expect.

echo hello # here is a very important command

What does this do?

echo hello : here is a very important command

The First Rule of Shell Programming

The shell parses a line into words, then tries to execute the first word on the line as a command, with the rest as arguments to that command. 

You'll gradually learn what "parses a line" means, but you can't be a shell programmer without keeping that rule in mind, from the start.

When bash parses a line, an early step is hunting for '#', then discarding it, and anything that follows. With that in mind, the different behaviors of the two echo commands above should make complete sense.

':' isn't a comment character, it's a command.

Here are two more examples to drive that home:

(1) This does what you expect:

#here is a very important comment

What does this do? (Think about it before you try it.)

:here is a very important comment

(2) This does what you expect:

# here's a very important comment

What does this do? (And what new does that tell you about the steps of parsing?)

: heres a very important comment

Even though shells now allow real comments, the colon command is still sometimes useful.  Thats a topic for the future.

For today, and from now on, use '#' interactively, not just in scripts and pay attention to 


Part 3.5
-----------------------------------
How about trying some examples, to convince yourself that you have command-line-editing under your fingers?

Type these lines.  You can check to see what happens after each command.

$ mkdir /tmp/bash-programming          # make a place to work
$ cd $_                                # go to it
$ for i in {a..e}; do >$i; done        # create some files   
$ for i in *; do mv $i $i.bak; done    # give them all extensions

That was pretty easy.  Pause to notice a few things.

You're writing loops right on the command line.

bash understands {a..e}, just as it understands {0..10}

$_ means "the last argument on the previous line." I think of it as a pronoun, and I pronounce $_ "it." The first two lines are "make a directory, then change to it."  Very useful.

When the shell is parsing a line, one of the first things it does is the redirects, creating files as needed. A new student will often try something like this:

$ sort mydata > mydata

That doesnt work, because the first thing bash does is the > mydata, which truncates mydata to 0 length. Next, bash runs the sort command on the now-empty file. 

The student then says, "Why didn't that work, and, uh, where did all my data go?"

Thats not a bug, its a feature. > mydata, all by itself without any command, just does the first step: it truncates mydata, and if it wasn't already there, it creates it, empty.

You could also say this:

$ for i in {a..e}; do touch $i; done           # create some files   

but thats not quite the same. touch will create a file if its not there, but if it was already there, it will just update the timestamp, and won't truncate it.

Quiz: How could you use a different redirection operator to do the same thing as touch?

Okay, you gave all the files a file extension with a one-liner. What if you want to remove the extension?

First, try your ideas on the command line:

$ echo foo.bak
foo.bak
$ echo foo.bak | sed 's/.bak//'
foo

Great! Something like that should work.

Next, recall the command and edit it, with vi commands, to loop through all your files.

$ for i in *; do $(echo foo.bak | sed 's/.bak//'); done
foo
foo
foo
foo
foo

Not quite. Recall that and fix it.

$ for i in *; do $(echo $i.bak | sed 's/.bak//'); done
a.bak
b.bak
c.bak
d.bak
e.bak

No, thats still not right. Why isn't it?  Oh. Sure. If $i is a.bak, then $i.bak is a.bak.bak, recall it and fix it again.

$ for i in *; do $(echo $i | sed 's/.bak//'); done
a
b
c
d
e

Aha! Those are the names you want to get to. Recall it again and say what you want to do.

$ for i in *; do mv $i $(echo $i | sed 's/.bak//'); done
$ ls
a b c d e

Sometimes, if youre doing something complex, you want to see what youre going to do before you do it. Here's how.

First, recall the loop to put extensions back on your files.

$ for i in *; do mv $i $i.bak; done

Now recall your command to rename them, and add another echo, so it looks like this:

$ for i in *; do echo mv $i $(echo $i | sed 's/.bak//'); done
mv a.bak a
mv b.bak b
mv c.bak c
mv d.bak d
mv e.bak e

Yep, that looks like what you want. Recall that command again.

Use ^A to append to the line, and pipe your commands to ... what?  To bash!

$ for i in *; do echo mv $i $(echo $i | sed 's/.bak//'); done | bash

Always remember: Bash isnt just a CLI or an interpreter to interpret scripts. It's a filter. It takes input from stdin, interprets it a line at a time, and writes to stdout.

When youre running it as a CLI, thats what its doing, too, of course. The bash connected to your terminal doesnt know that stdin is what youre typing and stdout is whats going to your screen. It's just processing its input, a line at a time.

You probably knew that, but creating commands on the fly and then piping them to bash to get them executed really drives that point home.

This style of programming -- growing a program on the command-line a little bit at a time, and seeing the output of each step before you add on the next piece -- is like watching the growth of a river delta. I think of it as alluvial programming.


This is part 3.5 because I had started a "How to Program in Bash, part 4," and decided I wanted to review a little first, piecing together some things I'd already talked about.

When I was a college freshman (that is, a 1st-year student at the university), in 1966, our class got to try out computers. At the time, computers were rare, and programs were written by punching holes in pieces of cardboard -- punch cards. 

Someone had spent the year before creating a language that could be written by typing instructions on a teletypewriter -- a teletype model 33 -- and we wrote little programs to let us analyze data from our physics laboratories. 

The language, CITRAN, required that you give every line a line number.  You didn't even need to type the lines of the program in order -- you could type line 50 first, then go back and type line 1, later.All control flow was done 

with GOTO statements. The line numbers were reals, not integers. If you discovered you needed to insert a line, say between line 10 and line 11, you could put in a line 11.5!










