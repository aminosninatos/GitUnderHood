Kafka
-------------
-------------


Source system(s) ---------------DATA------------->Target system(s)
(website events,pricing,logs)---KAFKA------->(database,Email system, Analytics)

Kafka theory
----------------------------------------------------------------------
Topics: is a particular stream of DATA (similar to table in database).
Topics are split into partitions.
Each message within a partition get an incremantal id called offeset.
Data is only kept a limited time (default is a week).

Brockers
---------------------------------------------------------------------
Kafka cluster is composed of many brockers(servers).
Brocker contains certain topic partitions because kafka is distributed.
Topics should have a replication factor > 1
Each partition have one leader brocker and multiple ISR(in-syc-replica).
Zookeeper decides who is the leader and ISR.

Producer
--------------------------------------------------------------------------------------------------------
Writes data to topics.
The load is balanced to many brockers due to partitions numbers.
The Producers can choose to receive acknowledgements(confirmation).
Producers can choose to send a key with a message so all messages for that key go to the same partition.

Consumer
--------------------------------------------------------------------
Consumers read data from a topic.
Data is read in order within each partitions.
Consumers read data in consumer groups.
Each consumer within a group reads data from exclusive partitions.

Consumer offsets
---------------------------------------------------------------------
Kafka stores the offeets at which a consumer group has been reading.
The offsets committed live in a kafka topic named __consumer_offsets.
