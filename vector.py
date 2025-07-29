# Importing necessary modules for embedding and vector store management
from langchain_ollama import OllamaEmbeddings  # Component 1: Embedding model to convert text into vector representation
from langchain_chroma import Chroma  # Component 2: Vector store for efficient search and retrieval
from langchain_core.documents import Document  # Component 3: Representation of documents (reviews in this case)
import os
import pandas as pd

# Reading restaurant review data from a CSV file
df = pd.read_csv("realistic_restaurant_reviews.csv")

# Initialize the embedding function using Ollama model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Define the location for the vector store (Chroma database)
db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)  # Check if the vector store already exists

# If documents are not already added, proceed with adding them to the vector store
if add_documents:
    documents = []
    ids = []

    # Looping through the dataset to create Document objects with relevant metadata
    for i, row in df.iterrows():
        document = Document(
                page_content=row["Title"] + " " + row["Review"],  # Combining title and review as content
                metadata={"rating":row["Rating"], "date": row["Date"]},  # Additional metadata like rating and date
                id=str(i)  # Unique document ID
            )
        ids.append(str(i))
        documents.append(document)

# Initializing the Chroma vector store to hold the documents and their vector embeddings
vector_store = Chroma(
        collection_name="restaurant_reviews",  # Name of the collection in the vector store
        persist_directory=db_location,  # Path to store the database
        embedding_function=embeddings  # Using the Ollama embeddings to convert text to vectors
    )

# Adding documents to the vector store if they haven't been added already
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

# Component 4: Retriever for querying the vector store and fetching relevant documents
retriever = vector_store.as_retriever(
        search_kwargs={"k":5}  # Returning top 5 most relevant documents
    )

