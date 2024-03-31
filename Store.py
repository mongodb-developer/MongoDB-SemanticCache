from pymongo import MongoClient
from langchain.vectorstores import MongoDBAtlasVectorSearch

client = MongoClient(params.mongodb_conn_string)
collection = client[params.db_name][params.collection_name]

# Insert the documents in MongoDB Atlas with their embedding
docsearch = MongoDBAtlasVectorSearch.from_documents(
    docs, embeddings, collection=collection, index_name=index_name
)
