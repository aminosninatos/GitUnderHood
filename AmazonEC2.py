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
When you stop the machine you lose your public IP address.

Security groups
---------------------------------------------------------------------------------------------------------------
Are acting as a firewall  on EC2 instances.
They regulate access ports, authorized IP ranges & control inbound and outbound trafiic.
One security group can be attached to multiple instaces.
Locked down to a region /vpv combination.
If your app is not accessible (time out) then its a security group issue.
If your app gives (connection refused )error then its an app error or its not launched. 

EC2 user data
---------------------------------------------------------------------------------------------
User data is a bootstrap script that is executed when the machine starts.
It is only run once when machine first starts not in reboots, stops or restarts.
This script can be run in the advanced details section when creating an instance. 

AMI
-------------------------------------------------------------
An image used to create our instance.
You can create your own AMI or use Public AMI .
AMI take space and lives in Amazon S3 storage.

Choosing EC2 instances
--------------------------------------------------------------------------------------------------------------------
You can use this website to get help : ec2instances.info
Burstable Instances (T2)  has Ok CPU performance but when the machine needs to process
something unexpected (spike in load) it can burst  and CPU can be very good.

Placement groups
---------------------------------------------------------------------------
Cluster : low latency 10Gbps network, same rack same availabality zone.
Spread  : spread across multiple availabality zones.
t2 instances dont support placement groups.

Elastic IPs
------------------------------------------------------------------------------------------------
When you stop and then start an EC2 instance, it can change its public IP.
if you need a fixed IP you need what we call an elastic IP.

Load balancers
----------------------------------------------------------------------------------------------------------------
Are servers that forward internet traffic to multiple servers(EC2 instances) to spread load.
ELB(EC2 load balancer) is a managed load balancer.
3 kinds of LBs ( Classic v1 - Application Lb v2 2016 - Network LB v2  2017).







