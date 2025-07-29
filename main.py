# Importing necessary modules for RAG implementation
from langchain_ollama.llms import OllamaLLM  # Component 1: Language Model (LM) for text generation
from langchain_core.prompts import ChatPromptTemplate  # Component 2: Prompt engineering for text generation
from vector import retriever  # Component 3: External knowledge retrieval (retriever)

# Initializing the model component for text generation (TinyLlama model used)
model = OllamaLLM(model="tinyllama")

# Defining a chat prompt template for answering restaurant-related questions
template = """
You are an expert in answering the questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

# Creating a prompt using the template
prompt = ChatPromptTemplate.from_template(template)

# Creating a chain that connects the prompt to the model for text generation
chain = prompt | model

# Loop to interact with the user and generate answers based on retrieved reviews
while True:
    print("\n\n----------------------------------------------------------")
    query = input("Ask your question (q to quit): ")
    if query == "q":  # Allowing user to exit the loop
        print("\nThanks for using, I hope you are answered for your queries :)\n")
        break
    print("\nOutput:")

    # Component 4: Retrieve relevant reviews using the retriever (RAG mechanism)
    reviews = retriever.invoke(query)  # Retrieve reviews based on the query

    # Passing retrieved reviews and the user's question to the chain for answer generation
    result = chain.invoke({
        "reviews": reviews,
        "question": query
    })

    # Displaying the generated answer
    print(result)

