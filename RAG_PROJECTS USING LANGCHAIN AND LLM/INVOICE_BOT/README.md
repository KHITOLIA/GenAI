# 🧾 Invoice Bot

[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-orange)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/RAG-LangChain-blue)](https://www.langchain.com)
[![FAISS](https://img.shields.io/badge/VectorDB-FAISS-green)](https://github.com/facebookresearch/faiss)
[![Ollama](https://img.shields.io/badge/LLM-Ollama%20(Mistral)-blueviolet)](https://ollama.com)
[![License](https://img.shields.io/badge/license-MIT-success)](LICENSE)

## 🔍 Project Description

**Invoice Bot** is a lightweight and interactive Retrieval-Augmented Generation (RAG) app built with **Streamlit**. It allows users to upload invoice PDFs, process them into chunks, embed the chunks using **HuggingFace embeddings**, store them in a **FAISS vector database**, and query specific invoice details using **Ollama's mistral model**.

This bot is particularly useful for:
- Extracting invoice numbers, total amounts, due dates, tax details, etc.
- Performing semantic search on invoice documents.
- Quickly answering questions about uploaded invoice PDFs.

---

## 🛠️ Tech Stack

| Component     | Tool/Library                                       |
|---------------|----------------------------------------------------|
| UI            | [Streamlit](https://streamlit.io/)                 |
| PDF Loader    | `PyPDFLoader` from `langchain_community`           |
| Text Splitter | `RecursiveCharacterTextSplitter` from LangChain    |
| Embeddings    | [HuggingFace Transformers](https://huggingface.co)|
| Vector Store  | [FAISS](https://github.com/facebookresearch/faiss)|
| LLM Backend   | [Ollama](https://ollama.com) with `mistral` model  |

---

## 📂 Folder Structure

```bash
InvoiceBot/
│
├── FAISS_DB/                  # Vector database folder (auto-created)
├── data/                      # Uploaded PDFs folder (auto-created)
├── invoice_bot.py             # Main Streamlit application
└── README.md                  # You are here
```

---

## 🚀 How It Works

1. **User Uploads Invoice PDF** using Streamlit interface.
2. The file is saved locally and split into text chunks.
3. Chunks are embedded using HuggingFace's `all-MiniLM-L6-v2`.
4. Chunks are stored in FAISS vector DB (if not already created).
5. On query, the vector DB is searched for similar content.
6. Retrieved context is passed to **Mistral** LLM via **Ollama** to generate an exact answer.

---

## 🧪 Example Query

```
"What's the total amount in invoice #123?"
```

**Response:**
> The total amount in invoice #123 is ₹12,450 only.

---

## ⚙️ Setup Instructions

1. **Install dependencies**
   ```bash
   pip install streamlit langchain faiss-cpu ollama sentence-transformers
   ```

2. **Run Ollama with Mistral**
   ```bash
   ollama run mistral
   ```

3. **Launch the Streamlit app**
   ```bash
   streamlit run invoice_bot.py
   ```

---

## 📌 Notes

- The vector DB is only created **once** per session unless the files or folders are cleared.
- You can delete the FAISS index and uploaded file using the **"🛑 Stop it's processing"** button in the UI.

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 🙋‍♀️ Need Help?

If you run into any issues or have questions about extending this project to more complex document types, feel free to ask!