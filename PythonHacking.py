Atom shortcuts to un/comment code
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

Scapy module
---------------------
is a python module that allows to send sniff and do a lot with network packets.
with python 3 we used it : import scapy.all as scapy.
to create an ARP packet : packet = scapy.ARP().
to view all fields of the ARP method : print(scapy.ls(scapy.ARP)).
to view a summary of the packet : print(packet.summary()).
to view a all packet fileds of the packet : print(packet.show()).
to send a packet : scapy.send(packet).
