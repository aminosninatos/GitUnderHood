Elasticsearch
----------------------
----------------------

Introduction
--------------------
Is Nosql distributed full-text database.
Elasticsearch stores data in documents of json strings & the schema is not required. 
Elasticsearch slices index into multiple shards. so they can be stored across multiple servers.

Elasticsearch schema
-----------------------------------------------------------
Elasticsearch has schema called mapping.
To get a list of indices:  GET /_cat/indices
To get an index mapping: GET index/_mapping
To get all documents in an index: GET index/type/_search


Types
------------------------------------------------------------------------
Elasticsearch has 5 data types: String,Boolean, Numbers, Date & Binary 

_Source
-------------------------------------------------------------------------------
To keep only the indexed version of the data by disabling the _source variable:
"_source" : {
	"enabled" : false
}
And store only the data we want : "store": true


Querying data
-----------------------------------------------------------------
Simple query : GET http://server:9200/index/_search?q=field:text

Domain Specific language (Query DSL)
--------------------------------------
GET http://server:9200/index/_search
{
   "query": {
      "match_all": {}
   }
}
The result with higher score comes first.
