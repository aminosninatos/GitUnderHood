Atom shortcuts
-----------------------------------------
To comment & uncomment we use : Cmd + /

Subprocess Module
--------------------
Using the call function of this module we can execute commands.
subprocess.call("Your_command").
to avoid hijacking code we can use:
subprocess.call(["command","argument1","argument2"])

Optparse module
---------------------
Allows us to get arguments for our python script.we use it like that:
parser = optparse.OptionParser()
parser.add_option("-x","--long_name_argument",dest=variable,help="help text here")
(options,arguments) = parser.parse_args()
options.x = x

Atom shortcut duplicate a line
--------------------------------
Cmd + Shift + D

Check_ouput function
------------------------
this function of the subprocess module allows to execute a command and catch the result in a variable.

Regular expression
-----------------------
we need to import re module and use the search function
re.search(r"Regular_expression",variable_to_search_within)
as a result we get an object and its first group contains the first match
result= object.group(0)
