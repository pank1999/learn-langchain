from langchain_core.prompts import PromptTemplate

template  = PromptTemplate(
    input_variables=["name"],
    template="What year did {name} win the Nobel Prize?",
    validate_template=True
)

template.save("nobel_prize_prompt.json")