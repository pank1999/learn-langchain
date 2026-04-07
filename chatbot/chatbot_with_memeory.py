from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_history = []

while True:
    user_input = input("Enter your prompt (or 'exit' to quit): ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input.lower() == 'exit':
        break

    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    response = model.invoke(chat_history)
    chat_history.append({"role": "assistant", "content": response.content})
    print("AI Response:")
    print(response.content)

print("Chat history:")
for message in chat_history:
    print(f"{message['role']}: {message['content']}")