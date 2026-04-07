from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
  repo_id="mistralai/Mistral-Nemo-Base-2407",
  max_new_tokens=100,
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of France?")

print(result)