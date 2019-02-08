Cassandra
---------------------------------------------------------------------------------------------------------------------------
keyspace -> database
column families -> tables.
Data are stored in memtables in memory then when a threshold is reachead data is flushed to disk in tables called sstables.


Partition key
--------------------------------------------------------------
can be the first part of the primary key.
can be the primary key is this primary key is not composite.

Sample Cassandra 
---------------------------------------------------------------------------------------------
> create keyspace "Name" with replication ={'class':'SimpleStrategy','replication_factor':3};
> use "Name";
> create table "users" ("username" text primary key,"email" text,"encrypted_pass" blob);

Cassandra does not support:
default values for columns.
data validation like length.
does not have the concept of NULL values.

Data types
----------------------------------------------------------------------------
text: stores encoded UTF-8 strings that have not length limit.
int: 32 bits integers signed so they can have (+) or (-).
float: 32 bits floating numbers.
timestamps: holds date & time values.
blob: unstructured binary data like images, audio or encrypted passwords. 

Purpose of data types
------------------------------------------------------------------------------------------------
input validation, if you want to insert text in place of integers Cassandra generates en error.
input for client libraries.
rows are ordered by the values of columns type.

Inserting data
----------------------------------------------------------------------------------------------------------------------
> insert into "users" ('username','email','encrypted_pass') values ('alice','alice@gmail.com',0xa6464ab86b866868686);

Compound primary key
------------------------------------------------------------------------------------------------------------
> create table "users_status" ("username" text,"id" timeuuid,"body" text,Primary key('username','id'));

Partition key : groups rows together into a logically related bundles.
clustering key : role is to determine the ordering of rows within a partition.
Compound keys represent a parent-child relationship, the partition key acts as a reference to the parent.
the clustering column uniquely identifies the rows among its siblings.

Cassandra structure
---------------------------------------------------------------------
> nodetool status KEYSPACE    to check the status of a keyspace.
data files are located in /var/lib/Cassandra.
log files are stored in /var/log/Cassandra.

Cassandra Backup & restore
--------------------------------------------------------------------------------------------
> nodetool snapshot KEYSPACE    to create a snapshot.
> nodetool listsnapshots     to list snapshots.
> nodetool clearsnapshot    to delete all old snapshots.

the backup process consists of copying all data files from the snapshot to the data folder.
Cassandra only restores data from a snapshot when the keyspace & tables schema exists.
then we use the command > nodetool refresh KEYSPACE TABLE.

Cassandra schema
--------------------------------------------------------------------
> cqlsh -e "DESC keyspace Name" > schema.cql
to save the schema of the keyspace Name.
> source 'schema.cql'
must be executed in the cqlsh command line to restore the schema.



















