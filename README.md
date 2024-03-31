## MongoDB-SemanticCache
How to use MongoDBAtlasSemanticCache to save on LLM costs

## Installation and Setup

See detailed configuration instructions.

We need to install the `langchain-mongodb` Python package:

pip install langchain-mongodb

python
Copy code

## Vector Store

See a usage example:

```python
from langchain_mongodb import MongoDBAtlasVectorSearch
LLM Caches
MongoDBCache
An abstraction to store a simple cache in MongoDB. This does not use Semantic Caching, nor does it require an index to be made on the collection before generation.

To import this cache:

python
Copy code
from langchain_mongodb.cache import MongoDBCache
To use this cache with your LLMs:

python
Copy code
from langchain_core.globals import set_llm_cache

# use any embedding provider...
from tests.integration_tests.vectorstores.fake_embeddings import FakeEmbeddings

mongodb_atlas_uri = "<YOUR_CONNECTION_STRING>"
COLLECTION_NAME="<YOUR_CACHE_COLLECTION_NAME>"
DATABASE_NAME="<YOUR_DATABASE_NAME>"

set_llm_cache(MongoDBCache(
    connection_string=mongodb_atlas_uri,
    collection_name=COLLECTION_NAME,
    database_name=DATABASE_NAME,
))
MongoDBAtlasSemanticCache
Semantic caching allows users to retrieve cached prompts based on semantic similarity between the user input and previously cached results. Under the hood, it blends MongoDBAtlas as both a cache and a vector store. The MongoDBAtlasSemanticCache inherits from MongoDBAtlasVectorSearch and needs an Atlas Vector Search Index defined to work. Please look at the usage example on how to set up the index.

To import this cache:

python
Copy code
from langchain_mongodb.cache import MongoDBAtlasSemanticCache
To use this cache with your LLMs:

python
Copy code
from langchain_core.globals import set_llm_cache

# use any embedding provider...
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
