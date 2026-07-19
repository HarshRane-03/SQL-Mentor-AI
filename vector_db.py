import os

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_groq import ChatGroq

from langchain_classic.chains import ConversationalRetrievalChain

from langchain_classic.memory import ConversationBufferMemory


loader = PyPDFLoader(r"C:\Users\raneh\OneDrive\Desktop\SQL master\MySQLNotesForProfessionals (1) (1).pdf")

documents = loader.load()



splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = splitter.split_documents(documents)



embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)



db = FAISS.from_documents(
    docs,
    embeddings
)

print("Vector DB Ready")

db.save_local("vectorstore")
print("Vector DB Saved Locally")