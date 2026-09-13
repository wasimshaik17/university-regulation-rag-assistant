import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from rag_pipeline import create_vector_store

st.set_page_config(page_title="University Regulation RAG Assistant", page_icon="🎓")
st.title("🎓 University Regulation RAG Assistant")

# ---- Sanity check: make sure the API key actually loaded ----
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error(
        "GOOGLE_API_KEY not found. Make sure you have a `.env` file in the "
        "same folder as this script with a line like:\n\n"
        "GOOGLE_API_KEY=your_key_here"
    )
    st.stop()


# ---- Load vector store (cached so it's built only once) ----
@st.cache_resource
def load_data():
    return create_vector_store("data")


try:
    vectorstore = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# ---- Gemini LLM ----
# As of mid-2026, Google has deprecated gemini-2.5-flash / gemini-pro
# for newer API keys. The current GA model is gemini-3.6-flash.
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.3,
    google_api_key=GOOGLE_API_KEY,
)

# ---- Prompt ----
system_prompt = (
    "Use the given context to answer the question. "
    "If you don't know the answer, say you don't know. "
    "Keep the answer simple and clear.\n\nContext: {context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# ---- Chain ----
qa_chain = create_retrieval_chain(
    retriever,
    create_stuff_documents_chain(llm, prompt),
)

# ---- UI ----
query = st.text_input("Ask your question:")

if query:
    with st.spinner("Thinking..."):
        try:
            result = qa_chain.invoke({"input": query})
        except Exception as e:
            st.error(f"Error: {e}")
        else:
            st.write("### ✅ Answer:")
            st.write(result["answer"])

            st.write("### 📄 Sources:")
            for doc in result.get("context", []):
                st.write(doc.metadata)