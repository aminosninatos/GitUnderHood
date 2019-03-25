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

