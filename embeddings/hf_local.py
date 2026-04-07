from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

query = "What is the capital of France?"
embedding = embeddings.embed_query(query)
print(str(embedding))