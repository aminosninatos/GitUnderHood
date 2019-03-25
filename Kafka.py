Kafka
-------------
-------------


Source system(s) ----------DATA------------->Target system(s)


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

