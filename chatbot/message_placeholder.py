from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# chat template
chat_template = ChatPromptTemplate([
    {"role": "system", "content": "you are a helpful support assistant agent."},
    MessagesPlaceholder(variable_name="chat_history"),
    {"role": "human", "content": "{query}"}
])

chat_history = []
#  load chat history
with open("chat_history.txt", "r") as f:
    chat_history.extend(f.readlines())
    
print("Chat history:", chat_history)

prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "What is the capital of France?"
})

print("Prompt:", prompt)

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
response = model.invoke(prompt)
print("Response:", response.content)