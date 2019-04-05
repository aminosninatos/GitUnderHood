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


Mappings
--------------------------------------------------------
is a schema definition:
$ curl -XPUT server:9200/index_name -d '
{
   "mappings": {

      "type_name": {
      				"_all":{"enabled":false},
      				"properties":{
      						       "year":{"type":"date"}
      				             }
                    }
                }
}'

To retreive the mappings:
$ curl -XGET server:9200/index_name/_mapping/type_name?pretty


Update a document
-------------------------------------------------------------------------
$ curl -XPOST server:9200/index_name/index_type/document_id/_update -d '
{
   "doc": {
            "filed_name":"value"
            }
}'

Every document haves a _version field, when you Update an existing document
a new document is created with an incrementd_version, the old document is 
marked for deletion.





















