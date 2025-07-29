from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="tinyllama")

template = """
You are an expter in answering the questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n----------------------------------------------------------")
    query = input("Ask your question (q to quit): ")
    if query =="q":
        print("\nThanks for using, I hope you are answered for your queries :)\n")
        break
    print("\nOutput:")
    
    reviews = retriever.invoke(query)
    result = chain.invoke({
        "reviews": reviews,
        "question": query
    })
    print(result)

