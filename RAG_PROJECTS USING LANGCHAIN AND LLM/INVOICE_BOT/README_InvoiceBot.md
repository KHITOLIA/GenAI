
# 🧾 Invoice Bot - RAG Powered Document Search Tool

Welcome to **Invoice Bot** – your intelligent assistant for understanding and extracting information from invoice documents! Built using **Streamlit**, **LangChain**, **FAISS**, and **Ollama**, this app uses **RAG (Retrieval-Augmented Generation)** to give you smart, accurate answers from your PDF files.

![Invoice Bot Banner](https://raw.githubusercontent.com/OpenAI/openai-cookbook/main/examples/images/langchain-rag.png)

---

## 🚀 Features

✅ Upload invoices in PDF format  
✅ Automatically extract and chunk the content  
✅ Create and store vector databases per file  
✅ Query the invoice using natural language  
✅ Powered by Mistral via Ollama (local LLM)  
✅ Clean, interactive Streamlit UI  
✅ Efficient: avoids recomputing if file already exists  

---

## 🛠️ Technologies Used

- **Streamlit** – for the UI
- **LangChain** – to handle document parsing & chunking
- **FAISS** – vector similarity search
- **HuggingFace Embeddings** – `all-MiniLM-L6-v2`
- **Ollama** – local LLM API for query generation (Mistral)
- **Python** – obviously 😄

---

## 📸 App Preview

![App UI](https://streamlit.io/images/brand/streamlit-mark-color.png)

---

## 🧰 Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/invoice-bot.git
cd invoice-bot

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install requirements
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

Make sure you have [Ollama](https://ollama.com/) and the `mistral` model pulled:

```bash
ollama pull mistral
```

---

## 📂 Directory Structure

```
invoice-bot/
│
├── app.py                # Main Streamlit app
├── Faiss/                # Folder where per-file vector DBs are stored
├── Data/                 # Uploaded files storage
└── README.md             # This file
```

---

## 🤖 Example Queries

- What is the total amount in invoice #102?
- Who is the buyer mentioned in this document?
- What date was the invoice issued?
- List all the items and quantities.

---

## 🧼 Reset / Cleanup

Click on **🛑 Stop it's processing** in the UI to clean up all uploaded files and vector DBs.

---

## ❤️ Credits

Made with 💡 by [Your Name].  
Built using [LangChain](https://www.langchain.com/), [Streamlit](https://streamlit.io/), and [Ollama](https://ollama.com/).

