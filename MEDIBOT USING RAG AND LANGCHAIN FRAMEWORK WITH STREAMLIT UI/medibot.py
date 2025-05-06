import streamlit as st
import json
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load Embedding Model and Vector DB
@st.cache_resource
def load_vector_store():
    embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    db = FAISS.load_local("database/faiss_database", embedding_model, allow_dangerous_deserialization=True)
    return db

db = load_vector_store()

# Initialize session state for conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# Streamlit UI
st.title("🧠 RAG Context Retriever with Memory")
st.markdown("This tool retrieves document chunks from a FAISS vector store and remembers previous queries and responses.")

# User Inputs
user_query = st.text_input("📝 Enter your Query", placeholder="e.g., What are the symptoms of diabetes?")
top_k = st.slider("🔎 Top-K Results", 1, 10, 3)

# Action Button
if st.button("Retrieve Context"):
    if user_query.strip() == "":
        st.warning("Please enter a valid query.")
    else:
        st.info("Searching vector store...")
        docs = db.similarity_search(user_query, k=top_k)

        if docs:
            response = [doc.page_content for doc in docs]
            # Save in session history
            st.session_state.history.append({
                "query": user_query,
                "results": response
            })

            st.success("Context Retrieved Successfully!")
            for i, res in enumerate(response, 1):
                with st.expander(f"📄 Match {i}"):
                    st.markdown(res)
        else:
            st.error("No matching context found.")

# Show Previous Conversations
if st.session_state.history:
    st.markdown("---")
    st.subheader("🕘 Conversation History")
    for i, entry in enumerate(st.session_state.history, 1):
        st.markdown(f"**Q{i}:** {entry['query']}")
        for j, res in enumerate(entry['results'], 1):
            st.markdown(f"- *Match {j}:* {res[:300]}...")  # trimmed preview

# Option to Download History
if st.session_state.history:
    history_str = json.dumps(st.session_state.history, indent=2)
    st.download_button("💾 Download Conversation History", history_str, file_name="conversation_history.json")
