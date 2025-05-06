from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import time

def type_log(message, delay = 0.005):
    print(f"[info] {message}")
    time.sleep(delay)

def type_output(text, delay = 0.0000005):
    for char in text:
        print(char, end = ' ', flush =True)
        time.sleep(delay)
    print("\n")       

# Load the FAISS database from the Directory
db_faiss_path = "database/faiss_database"

embedding_model = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
faiss_db = FAISS.load_local(db_faiss_path, embedding_model, allow_dangerous_deserialization=True)
print("FAISS database loaded from : ", db_faiss_path)

# step 2: retrieve the most relevant documents

def retrieve_documents(query):
    docs = faiss_db.similarity_search(query)
    return docs

print("_"*60)
user_query = input("Enter your query to retrieve the most relevant data from PDF documents : ")
type_log("Retrieving documents...")
retrived_documents = retrieve_documents(user_query)

print("_"*60)
print("Retrieved Documents:")
for i, doc in enumerate(retrived_documents):
    print(f" Retrived Document {i} :{doc.page_content}\n")
