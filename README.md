# Notice: Repository Deprecation
This repository is deprecated and no longer actively maintained. It contains outdated code examples or practices that do not align with current MongoDB best practices. While the repository remains accessible for reference purposes, we strongly discourage its use in production environments.
Users should be aware that this repository will not receive any further updates, bug fixes, or security patches. This code may expose you to security vulnerabilities, compatibility issues with current MongoDB versions, and potential performance problems. Any implementation based on this repository is at the user's own risk.
For up-to-date resources, please refer to the [MongoDB Developer Center](https://mongodb.com/developer).


## MongoDB-SemanticCache 🍃 🦜 ⛓️
How to use MongoDBAtlasSemanticCache to save on LLM costs

## Installation and Setup

We need to install the `langchain-mongodb` Python package:

pip install langchain-mongodb

## Vector Store

See a usage example:

```
from langchain_mongodb import MongoDBAtlasVectorSearch
```
An abstraction to store a simple cache in MongoDB. This does not use Semantic Caching, nor does it require an index to be made on the collection before generation.

To import this cache:
```
from langchain_mongodb.cache import MongoDBCache
```
To use this cache with your LLMs:
```
from langchain_core.globals import set_llm_cache
```
## use any embedding provider...
```
from tests.integration_tests.vectorstores.fake_embeddings import FakeEmbeddings

mongodb_atlas_uri = "<YOUR_CONNECTION_STRING>"
COLLECTION_NAME="<YOUR_CACHE_COLLECTION_NAME>"
DATABASE_NAME="<YOUR_DATABASE_NAME>"

set_llm_cache(MongoDBCache(
    connection_string=mongodb_atlas_uri,
    collection_name=COLLECTION_NAME,
    database_name=DATABASE_NAME,
))
```
## MongoDBAtlasSemanticCache
Semantic caching allows users to retrieve cached prompts based on semantic similarity between the user input and previously cached results. Under the hood, it blends MongoDBAtlas as both a cache and a vector store. 

The MongoDBAtlasSemanticCache inherits from MongoDBAtlasVectorSearch and needs an Atlas Vector Search Index defined to work. Please look at the usage example on how to set up the index.

To import this cache:
```
from langchain_mongodb.cache import MongoDBAtlasSemanticCache
```
from langchain_core.globals import set_llm_cache
```
# use any embedding provider...
```
```
from tests.integration_tests.vectorstores.fake_embeddings import FakeEmbeddings

mongodb_atlas_uri = "<YOUR_CONNECTION_STRING>"
COLLECTION_NAME="<YOUR_CACHE_COLLECTION_NAME>"
DATABASE_NAME="<YOUR_DATABASE_NAME>"

set_llm_cache(MongoDBAtlasSemanticCache(
    embedding=FakeEmbeddings(),
    connection_string=mongodb_atlas_uri,
    collection_name=COLLECTION_NAME,
    database_name=DATABASE_NAME,
))
```
