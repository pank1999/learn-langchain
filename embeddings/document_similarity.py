from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)

documents = [
    "The cat is on the roof.",
    "The dog is in the yard.",
    "The bird is flying in the sky.",
    "The cat is sleeping on the couch.",
    "The dog is barking at the mailman."
]

query = "Where is the cat?"

# Generate embeddings for the documents and the query
document_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# Compute cosine similarity between the query and each document
similarities = cosine_similarity([query_embedding], document_embeddings)[0]

print("Similarity scores:", similarities)

# Get the index of the most similar document
most_similar_index = np.argmax(similarities)
most_similar_document = documents[most_similar_index]

print(f"Query: {query}")
print(f"Most similar document: {most_similar_document}")
print(f"Similarity score: {similarities[most_similar_index]:.4f}")