from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
query = "What is the capital of France?"
embedding = embeddings.embed_query(query)
print(str(embedding))