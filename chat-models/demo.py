from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
result = model.invoke("what is the capital of india ?")
print(result.content)


# temperature is a parameter that controls the randomness of the output. Higher values (e.g., 0.9) will make the output more random, while lower values (e.g., 0.2) will make it more focused and deterministic.
# Lower temperature values will make the model more likely to choose the most probable next word, while higher values will allow for more creativity and diversity in the output.
# eg: If you set temperature to 0.2, the model will be more likely to generate a response that is similar to the training data, while if you set it to 0.9, the model may generate a more unique and creative response.