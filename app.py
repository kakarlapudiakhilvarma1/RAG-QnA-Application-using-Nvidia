import streamlit as st
import os

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.output_parsers import StrOutputParser

## Let's get the env variables.
from dotenv import load_dotenv
load_dotenv()

## loading Nvidia API Key
os.environ['NVIDIA_API_KEY'] = os.getenv("NVIDIA_API_KEY")

## load the LLM model
llm = ChatNVIDIA(model="meta/llama3-70b-instruct")

## Function of 
def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = NVIDIAEmbeddings()
        st.session_state.loader = PyPDFDirectoryLoader("./us_census")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=50)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:30])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)


## Streamlit App
st.set_page_config(page_title="Nvidia NIM Q&A - RAG", page_icon="🚀")
st.title("Nvidia NIM Q&A - RAG Application 🚀")

prompt = ChatPromptTemplate.from_template(
""" 
Answer the questions based on provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Question:{input}

"""
)

prompt_1 = st.text_input("Enter your question from Documents")

if st.button("Embed the docs & Fetch Answer"):
    vector_embedding()
    st.success("FAISS Vector Store DB is Ready using NvidiaEmbedding!!!")


import time
if prompt_1:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    start = time.process_time()
    response = retrieval_chain.invoke({'input': prompt_1})
    print("Response time :", time.process_time()-start)
    st.write(response['answer'])


    ## With streamlit expander
    with st.expander("Document Similarity Search"):
        # find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("------------------------------")



