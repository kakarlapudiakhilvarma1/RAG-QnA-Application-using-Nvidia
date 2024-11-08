# Nvidia NIM Q&A - RAG Application 🚀

This repository contains a **Streamlit**-based application that implements a **Retrieval-Augmented Generation (RAG)** system for answering questions from documents, powered by **NVIDIA's Embedding API** and **Langchain**. It leverages **FAISS vector store** to index documents and retrieve the most relevant information to answer user queries.

## Features ✨

- 📄 Upload and process a directory of PDF documents.
- 🧩 Split the documents into smaller chunks for efficient retrieval.
- 🔑 Use NVIDIA's language models and embeddings to perform semantic search.
- 🤖 Answer questions based on the content of the documents.
- 🔍 Display relevant document snippets for context in the response.
- ⚡ Optimized for processing large documents via **FAISS** and efficient embeddings.

## Requirements 🛠️

Before running the application, ensure you have the following installed:

- Python 3.7 or higher 🐍
- Streamlit 🌐
- Langchain 📚
- FAISS 🔎
- NVIDIA's embeddings and language model APIs 🌟
- `python-dotenv` for managing environment variables 📄

## Setup 🏗️

### 1. Clone the repository

```bash
git clone https://github.com/your-username/nvidia-nim-qa.git
cd nvidia-nim-qa
```

### 2. Install the dependencies

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes the following dependencies:

```txt
streamlit
langchain
langchain-community
faiss-cpu
langchain-nvidia-ai-endpoints
python-dotenv
```

### 3. Set up environment variables 🔑

You'll need an API key from NVIDIA to access the embedding and language model services.

1. Create a `.env` file in the root of the repository.
2. Add your **NVIDIA API key** to the `.env` file:

```dotenv
NVIDIA_API_KEY=your_nvidia_api_key
```

### 4. Prepare your documents 📁

Ensure your PDF documents are placed in a directory named `./us_census/` or adjust the path accordingly in the script.

### 5. Run the Streamlit app 🚀

Once everything is set up, run the Streamlit app with the following command:

```bash
streamlit run app.py
```

This will launch the app in your browser, where you can interact with the Q&A system.

## Usage 📝

### 1. Embed Documents 📚

- **Click** the "Embed the docs & Fetch Answer" button to load your documents and prepare them for embedding.
- The documents will be processed using **NVIDIA's embeddings** and indexed using **FAISS** for efficient retrieval.

### 2. Ask Questions ❓

- Enter a question in the input field labeled **"Enter your question from Documents"**.
- The application will retrieve relevant document chunks using FAISS and NVIDIA's language model.
- The answer to your question, along with relevant context from the documents, will be displayed.

### 3. Document Similarity Search 🔍

- The **Document Similarity Search** section shows the document chunks retrieved that were most relevant to your query.
- This allows you to see the exact content the model used to answer your question.

## Application Execution 🚀

### Initial Page 🖥️

Upon loading the application, you will be greeted with an interface where you can input your questions based on the documents that have been added to the application. Here's how to proceed:

1. **Enter your question**: In the input box labeled **"Enter your question from Documents"**, type in your query.
   
2. **Click "Embed the docs & Fetch Answer"**: After entering your question, click the button **Embed the docs & Fetch Answer**. This will load and embed the documents, prepare the FAISS vector store, and fetch the relevant answers based on the provided context.

3. **Answer Display**: Once the process completes, the app will provide you with an answer derived from the documents.

4. **Expand Similarity Search**: You can also expand the **Document Similarity Search** section to view the specific context or chunks from the documents that were used to generate the answer.

This section gives you the ability to see from where the model has derived its response, making the application highly transparent and easy to understand.

## Output Screenshots 📸

Here are a few sample outputs to illustrate how the application works:

1. **Initial Page View**:
  ![image](https://github.com/user-attachments/assets/80951c22-78d2-41ed-bf43-efd718f8eace)

   - The user interface where you can enter your questions and interact with the app.

2. **Question Answering**:
   ![image](https://github.com/user-attachments/assets/21e548c7-cafc-4022-bcca-02735c9641ae)

   - Example of the answer displayed after processing the documents and retrieving relevant content.

3. **Document Similarity Search**:
   ![image](https://github.com/user-attachments/assets/50c0c900-c3ce-4ed1-86c5-1e3f2d6f430b)

   - Expanded section showing the document chunks that were used for generating the answer.

## Code Overview 👨‍💻

### Main Components 🛠️

1. **PyPDFDirectoryLoader**: Loads PDF files from a specified directory (`./us_census/`).
2. **RecursiveCharacterTextSplitter**: Splits documents into smaller chunks for more effective retrieval.
3. **NVIDIAEmbeddings**: Uses NVIDIA's API to create embeddings from text.
4. **FAISS**: A vector database to store and retrieve document embeddings.
5. **ChatNVIDIA**: The language model that generates answers based on retrieved document chunks.
6. **Langchain**: Manages document retrieval and the interaction between components.

### Workflow 🔄

1. **Document Loading**: The `vector_embedding()` function loads and splits documents.
2. **Question Answering**: The question is passed to the `retrieval_chain`, which retrieves relevant document chunks and then generates an answer using the language model.
3. **Display**: The answer is displayed, and document snippets are shown in an expandable section for context.

## Contributing 🤝

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## Acknowledgements 🙏

- **Langchain**: For providing powerful tools for document processing and retrieval.
- **NVIDIA**: For their advanced AI and embeddings API.
- **FAISS**: For fast and efficient vector similarity search.
- **Streamlit**: For easy deployment of interactive web applications.

---
