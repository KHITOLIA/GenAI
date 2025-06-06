import streamlit as st
from llm import policy_bot
import os
import shutil
import requests
from pathlib import Path



db_faiss_path = 'HR_POLICY_DATABASE'
os.makedirs(db_faiss_path, exist_ok=True)  # this wil generate the folder if does not exist


st.title('Policy Bot')
st.markdown("RAG Application to retrieve relevant information for HR department")

st.header('Ask your question about HR policy : ')
url = st.text_input("please provid me the link of the HR Policy pdf document:")

if url:
    response = requests.get(url)
    if response.status_code == 200:
        file_bytes = response.content
        file_name = url.split("/")[-1]

        st.download_button(
            label="Download HR Policy PDF",
            data=file_bytes,
            file_name=file_name,
            mime="application/pdf"
        )

user_query = st.text_input("Enter your question here:")
if st.button('🔍Retrieved Content'):
    if user_query.strip() == "":
        st.warning("Please enter a valid query.")
    else:
        try:
            response = policy_bot(user_query, url)
            st.success("Documents retrieved successfully!")
            st.subheader('Retrieved Document:')
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred while processing your query: {e}")    

if st.button('Stop'):
    if os.path.exists(db_faiss_path):
        try:
            shutil.rmtree(db_faiss_path)
        except Exception as e:
            st.warning(f"Could not delete folder {db_faiss_path}: {e}")
    os._exit(0)