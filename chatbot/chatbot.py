from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# This is a simple command-line chatbot that uses the ChatOpenAI model to generate responses based on user input.
# Problem : It does not have memory, so it cannot remember previous interactions or context.

while True:
    user_input = input("Enter your prompt (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    response = model.invoke(user_input)
    print("AI Response:")
    print(response.content)