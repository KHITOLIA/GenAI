from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# file_path = "https://info.microsoft.com/rs/157-GQE-382/images/Digital%20Workplace%20for%20HR_Supercharging%20HR%20with%20Data.pdf"

db_faiss_path = 'HR_POLICY_DATABASE'
def load_and_split_documents(file_path):
    # load the pdf document
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()
    # split the documents into smaller chunks

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=500)
    split_documents = text_splitter.split_documents(documents)
    return split_documents

# chunks = load_and_split_documents(file_path)

def create_vector_store(chunks):

    # craete embeddings
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db_faiss = FAISS.from_documents(chunks, embedding=embedding_model)
    db_faiss.save_local(db_faiss_path)
    return db_faiss

# db = create_vector_store(chunks)


def retrieving_documents(query, file_path):
    chunks = load_and_split_documents(file_path)
    db = create_vector_store(chunks)
    # load the vector store
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(db_faiss_path, embedding_model, allow_dangerous_deserialization=True)
    # retireve the documents
    retrieved_doc = db.similarity_search(query,k = 1)[0].page_content
    return retrieved_doc

# retrieved_document = retrieving_documents("What are the benefits of using data in HR?")
# print(retrieved_document)
