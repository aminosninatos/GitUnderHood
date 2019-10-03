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
