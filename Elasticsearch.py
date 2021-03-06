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

Deleting a document
----------------------------------------------------------------
$ curl -XDELETE server:9200/index_name/index_type/document_id


Using Analyzers
-----------------------------------------------------------------
Sometimes text fields should be exact match:
then we use no_analyzer mapping
Search on analyzed fields will return anything remotely relevant:
deponding on the Analyzer, result will be case-insensitive,stemmed
stopwords removed,synonyms applied etc.


Query line Search
---------------------------------------------------------------------------------
$ curl -XGET server:9200/index_name/index_type/_search?q=filed_name:value&pretty


Request body Search
-------------------------------------------------------------------
$ curl -XGET server:9200/index_name/index_type/_search?pretty -d '
{
   "query": {

            "match" : {
                        "filed_name":"value"
                      }
            }
}'     


Phrase Search
---------------------------------------------------------------------
must find all the terms in the right order
$ curl -XGET server:9200/index_name/index_type/_search?pretty -d '
{
   "query": {

            "match_phrase" : {
                        "filed_name":"value"
                      }
            }
}'     


Slop
-----------------------------------------------------------------------------------------
the order matters but you are OK with some terms in between
the slop means how far you are willing to let the term moves to satisfy the phrase Search
$ curl -XGET server:9200/index_name/index_type/_search?pretty -d '
{
   "query": {

            "match_phrase" : {
                        "filed_name":{query:"value","slop":1}
                      }
            }
}'     


Changing mappings
------------------------------------------------------------------------------------------------------
you cannot change a mappings on an existing index, you would have to delete it, set up a new mappings.
like the number of shards this is somthing you have to think about before importing data to your index.

Fuzzy matches
-----------------------------------------------------------
Is a way to account for typos and misspellings.
for an edit distance of 1 (fuziness=1).
- substitution of characters (interstellar->intersteller).
- insertiond of characters (interstellar->instersteller).
- deletion of characters (interstellar->intersteler).


$ curl -XGET server:9200/index_name/index_type/_search?pretty -d '
{
   "query": {

            "fuzzy" : {
                        "filed_name":{"value":"search_value","fuziness":1}
                      }
            }
}'     


Prefix query
--------------------------------------------------------------------
$ curl -XGET server:9200/index_name/index_type/_search?pretty -d '
{
   "query": {

            "prefix" : {
                        "filed_name":"prefix_value"
                      }
            }
}'     


Wildcard query
--------------------------------------------------------------------
$ curl -XGET server:9200/index_name/index_type/_search?pretty -d '
{
   "query": {

            "wildcard" : {
                        "filed_name":"value*"
                      }
            }
}'     


Search as you type
--------------------------------------------------------------------
$ curl -XGET server:9200/index_name/index_type/_search?pretty -d '
{
   "query": {

            "match_phrase_prefix" : {
                        "filed_name":{"query":"search_value","slop":10}
                      }
            }
}'     


Logstash
---------------------------------------------------------------------------------------------------------------------
Logstash is an open source data collection engine with real-time pipelining capabilities. 
Logstash can dynamically unify data from disparate sources and normalize the data into destinations of your choice.
after adding the Elasticsearch repos, we can install it :
> apt install logstash
then we configure the config file in /etc/logstash/conf.d/logstash.conf according to input and output we want:
for example to feed apache access log files to Elasticsearch, logstash.conf should be:

input { 
		file {
		    path => "/tmp/access_log"
		    start_position => "beginning"
		    ignore_older => 0
		    }
      }

filter {
  grok {
    match => { "message" => "%{COMBINEDAPACHELOG}" }
  }
  date {
    match => [ "timestamp" , "dd/MMM/yyyy:HH:mm:ss Z" ]
  }
}

output {
  elasticsearch { hosts => ["localhost:9200"] }
  stdout { codec => rubydebug }
}



Elasticsearch aggregations
------------------------------------------------------------------------------------------------
The aggregations framework helps provide aggregated data based on a search query.
It is based on simple building blocks called aggregations, that can be composed in order to build 
complex summaries of the data.
the syntax is as follows:
$ curl -XGET server:9200/index_name/index_type/_search?size=0&pretty -d '
{
   "aggs" : {
    "<aggregation_name>" : {
        "<aggregation_type>" : {
            <aggregation_body>
        }
        [,"meta" : {  [<meta_data_body>] } ]
        
}'     














