# RAG-based Language Model App

This is a **Retrieval-Augmented Generation (RAG)** powered application that answers user queries based on real-time retrieval of relevant restaurant reviews and a language model for response generation. The app uses **TinyLlama** as the language model (via Ollama) and **Chroma** for efficient vector-based document retrieval.

## Components
1. **Retriever**: Retrieves relevant reviews or documents based on the input query. Uses **Chroma** and **OllamaEmbeddings** for document storage and retrieval.
2. **Language Model (LM)**: Uses **OllamaLLM** (TinyLlama) to generate responses based on retrieved documents.
3. **Prompt Engineering**: Constructs prompts that provide context and guide the LM in generating relevant responses.

## Requirements

Before running the app, make sure you have the following installed:

- **Python 3.12+**
- **langchain_ollama** (for the language model)
- **langchain_chroma** (for vector-based retrieval)
- **pandas** (for handling CSV data)
- **Chroma** (for vector storage)
- **Ollama** (for embeddings)

## Setup
1. Clone the repository or download the project files:
```bash
git clone https://github.com/AbhishekSinghPursuit/RAG-app.git
```
2. Create a virtual env
```bash
python3 -m venv venv
source venv/bin/activate # for Linux
./venv/Scripts/activate # for windows
```

3. Install the required packages using:

```bash
pip3 install -r requirements.txt
```

4. Ensure that your environment has the necessary libraries installed.

5. Make sure you have realistic_restaurant_reviews.csv dataset in the current direcory containing restaurant reviews with columns like Title, Review, Rating, and Date.

6. Install Ollama
  - For windows, go to this url: https://ollama.com/download
  - For Linux, run command:
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```

7. After installing Ollama, confirm the installation:
   ```bash
   ollama --version
   ollama list      # no models are there
   ```
8. Install the *TinyLLaMA* and *mxbai-embed-large* using ollama
   ```bash
   ollama pull tinyllama:latest
   ollama pull mxbai-embed-large
   ollama list
   ```
10. Run the application with:

```bash
python3 main.py
```

## Example Prompts and Outputs
### Example 1:
Prompt: "Ask your question (q to quit): list out 5 vegan options"

Output:
```bash
Output:
1. "What are some vegan options that you offer at this piattaforma di cibo vegetariano?"
2. "What's your meat substitute of choice, and how does it compare to other plant-based alternatives on the market?"
3. "Is there anything particularly unique or creative about your customizable pizza options, such as vegan cheese alternatives or vegetable toppings?!"
4. "Do you have any gluten-free or low-carb options available? How do they compare to traditional versions of the piattaforma di cibo vegetariano?"
5. "Which non-dairy milk alternatives are most commonly used in this area? Are there any unique options, such as coconut milk or almond milk?!"
```
### Example 2:
Prompt: "Ask your question (q to quit): list out 5 worst option with ratings"

Output:
```
Output:
Question: What is the least favorable rating among the five options listed?

Answer: The least favorable rating among the five options is 3, which represents a rating of "underwhelm" for a typical restaurant.
```

## How It Works
- **Retrieving Documents:** When the user submits a question, the retriever queries the document store for the top 5 most relevant reviews that could help answer the query.
- **Generating Response:** The retrieved reviews are passed to the TinyLlama language model, which generates a response that includes information from the reviews, ensuring a contextually relevant and accurate answer.
- **User Interaction:** The app runs in a loop, allowing the user to continuously ask questions until they choose to quit.

## Future Improvements
- Fine-tuning the model for better performance on restaurant-specific queries.
- Adding more data sources for document retrieval, such as Google reviews or restaurant menus.
- Optimizing retrieval speed and reducing latency for larger datasets.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

