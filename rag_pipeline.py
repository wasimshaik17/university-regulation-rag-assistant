import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

# PDF loader
from langchain_community.document_loaders import PyPDFLoader

# Text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

# Vector store
from langchain_community.vectorstores import FAISS


def create_vector_store(data_path: "str" = "data") -> Optional[object]:
    """Create a FAISS vectorstore from all PDFs in data_path using
    local HuggingFace embeddings (no API key required for this part)."""

    if not os.path.isdir(data_path):
        raise FileNotFoundError(f"Folder '{data_path}' not found")

    documents = []

    for file in os.listdir(data_path):
        if file.lower().endswith(".pdf"):
            path = os.path.join(data_path, file)
            loader = PyPDFLoader(path)
            docs = loader.load()
            documents.extend(docs)

    if not documents:
        raise ValueError(f"No PDFs found in '{data_path}' folder")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore