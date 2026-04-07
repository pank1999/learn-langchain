from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

# Example using HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="google/flan-t5-small",
    task="text2text-generation",
    pipeline_kwargs={"max_length": 512, "num_beams": 4,}
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of France?")
print(result)