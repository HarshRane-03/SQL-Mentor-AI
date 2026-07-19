import os
import streamlit as st

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()

# Read Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="SQL Mentor AI",
    page_icon="🤖"
)

st.title("🤖 SQL Mentor AI")

@st.cache_resource
def load_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db

db = load_vectorstore()

retriever = db.as_retriever(
    search_kwargs={"k": 4}
)

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input(
    "Ask SQL Questions..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an SQL Tutor.

Answer the question using the context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    answer = response.content

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)