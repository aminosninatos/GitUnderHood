AMAZON EC2
------------------
------------------


AWS is a cloud provider.
EC2 is the main service to provide machines on demand.

EC2 basics
--------------------------------------------------------------------
Renting virtual machines(EC2).
Storing data on virtual drives(EBS).
Distruibuting load across machines(ELB).
Scaling the services using auto scaling groups(ASG).

EC2 instances
---------------------------------------------------------------------------------------------------
You will pay for instances that are running so stop an instance to save money.
When you terminate an instance it is completely removed and all data on it.
To use the private key file to access the instance : > chmod 400 keyfile.pem

Security groups
---------------------------------------------------------------------------------------------------------------
Are acting as a firewall  on EC2 instances.
They regulate access ports, authorized IP ranges & control inbound and outbound trafiic.
One security group can be attached to multiple instaces.
Locked down to a region /vpv combination.
If your app is not accessible (time out) then its a security group issue.
If your app gives (connection refused )error then its an app error or its not launched. 