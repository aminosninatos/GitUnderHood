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

Bootstrap servers
-----------------------------------------------------------------------------------
That means that you need only to connect to one broker to connect to all brockers.
Each broker knows about all brockers, topics and partitions.

Zookeeper
--------------------------------------------------------
Manages brockers and helps performing leader election.
Sends notifications to kafka in case of changes.
Kafka cannot work without Zookeeper.
Zookeeper works with odd number of servers(3,5,7...).

Kafka command line interface
------------------------------------------------------------------------------------------------------------
To create a topic:
> kafka-topics --zookeeper 127.0.0.1:2181 --topic topic-name --create --partitions 3 --replication-factor 2
To list topics:
> kafka-topics --zookeeper 127.0.0.1:2181 --list
To describe a topic:
> kafka-topics --zookeeper 127.0.0.1:2181 --topics topic-name --describe
To delete a topic:
> kafka-topics --zookeeper 127.0.0.1:2181 --topics topic-name --delete

Kafka console Producer command line
------------------------------------------------------------------------------------------------------
To create a Producer:
> kafka-console-producer --broker-list 127.0.0.1:9092 --topic topic-name --producer-proprety acks=all

Kafka console consumer command line
-----------------------------------------------------------------------------------------------
To create a consumer:
> kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic topic-name --from-beginning

Kafka console consumer in groups command line
---------------------------------------------------------------------------------------------------
To create a consumer in a group:
> kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic topic-name --group my-first-app

Kafka  consumer group command line
----------------------------------------------------------------------------------------
To list all consumer groups:
> kafka-consumer-groups --bootstrap-server 127.0.0.1:9092 --list
To describe a consumer group:
> kafka-consumer-groups --bootstrap-server 127.0.0.1:9092 --describe -group group-name

Resetting offsets
-----------------------------------------------------------------------------------------------------------------------------------------
To reset offsets:
> kafka-consumer-groups --bootstrap-server 127.0.0.1:9092 --group my-first-app --reset-offsets --to-earliest --execute --topic topic-name

Starting zookeeper
-------------------
> zookeeper-server-start.bat .\config\zookeeper.properties

Starting kafka
-----------------
>  kafka-server-start.bat .\config\server.properties

Kafka connect API
--------------------
Simplify and improve getting data in and out of kafka.
Simplify transforming data within kafka without relying on external libs.
Source connectors : to get data from common data sources.
Sink connectors : to publish data in common data stores.
most of the time we use connectors from Confluent.

Kafka Streams
--------------
Easy data processing and transformaton library within Kafka.
It gets data from kafka and put it back to kafka.
