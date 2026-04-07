from langchain_core.prompts import ChatPromptTemplate

# This is a simple example of how to use the ChatPromptTemplate to create a prompt for a chatbot.
chat_template = ChatPromptTemplate([
    {"role": "system", "content": "You are a helpful {domain} assistant."},
    {"role": "human", "content": "What is the capital of France?"}
])

chat_prompt = chat_template.invoke({"domain": "geography"})
print(chat_prompt)

