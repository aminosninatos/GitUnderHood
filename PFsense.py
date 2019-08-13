PFsense Tips and Tricks
----------------------------
----------------------------


OpenVPN Steps
--------------------------------------------------------------
1- Create a Certificate Authority on PFsense (CA).
2- Create an OpenVPN Server certificate.
3- Configure an OpenVPN Server on PFsense.
4- Configure an OpenVPN Client Access on PFSense.
5- Install the OpenVPN Client Export Package.
6- Add the VPN User.
7- Download the Client Configuration using to Client Export. 
NB : in order to access all devices in your LAN via VPN they should all be configured with pfsense LAN interface
as default gateway.

DNSBL
--------------
In order to work with DNSBL, all your clients should use PFSense as the default DNS resolver.
You can implement that using a firtewall rule that allows only traffic to port 53 on the LAN net.
You have then you provide a list of blacklisted site from PI-HOLE or Steven Black Github repositories.
