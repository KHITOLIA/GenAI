from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import requests
from langchain.llms import Ollama


# loader = PyMuPDFLoader("data\AbhishekWAI.pdf")
# oata = loader.load_and_split()
# text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500, 
#         chunk_overlap=50,
#         length_function=len
#     )
# text_chunks = text_splitter.split_documents(data)

embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
# vectorstore = FAISS.from_documents(text_chunks, embedding=embedding_model)
# vectorstore.save_local("Faiss")

db = FAISS.load_local("Faiss", embeddings=embedding_model, allow_dangerous_deserialization=True)

query = "what's your experience in Data Science"
similar_query = db.similarity_search(query, k=1)[0].page_content
print(similar_query)

llm = Ollama(model = 'llama3.2')
prompt_template = """Hi, your name is Hr_bot generated by Tushar khitoliya : Give me the {query} from HR poclicy in {similar_query}. No irrelevant info. 
             Provide me the exact information in words only. or higlight the relevant information 
             Please provide the answer in a Bulletin Point by focusing on the main topics to cover! 
             after proving the information you can ask me for the next query ?."""
prompt = prompt_template.format(query=query, similar_query=similar_query)
output = llm.invoke(prompt)
print(output)


