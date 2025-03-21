# AI-Powered Text Processing Pipeline

## 📌 Overview
This project is an **AI-powered text processing pipeline** that automates:
- **Text extraction** from TXT, PDF, and DOCX files
- **Text cleaning** (removing noise, stopwords, special characters)
- **Summarization** (extractive summaries using transformers)
- **Chunking** (splitting long text for better processing)
- **Embedding** (using OpenAI or local sentence transformers)
- **Retrieval-Augmented Generation (RAG)** (for AI-powered search & Q&A)
- **Cloud storage** (Google Drive integration)
- **Auto-processing** (detects and processes newly uploaded files)

---

## 🛠️ Features
### 🔹 **File Support**
- Supports **TXT, PDF, and DOCX** file formats.
- Uses **LangChain document loaders** for structured text extraction.

### 🔹 **Text Processing**
- **Cleaning**: Converts text to lowercase, removes special characters and stopwords.
- **Summarization**: Generates concise summaries with `transformers`.
- **Chunking**: Splits text into smaller chunks for embeddings.

### 🔹 **Embeddings & RAG**
- Uses **FAISS** and **Pinecone** for **vector storage**.
- Enables **AI-powered retrieval** via OpenAI models.

### 🔹 **Cloud Storage & Automation**
- **Google Drive integration** for uploading processed files.
- **Auto-processing**: Detects new files and runs the pipeline automatically.

---

## 🚀 How to Use

### 1️⃣ **Install Dependencies**
Run the following command in your Jupyter Notebook or terminal:
```bash
!pip install nltk sentence-transformers transformers openai pinecone-client faiss-cpu langchain pypdf python-docx watchdog google-auth google-auth-oauthlib google-auth-httplib2 googleapiclient pydrive2
```

### 2️⃣ **Run the Jupyter Notebook**
Download and open:  
📥 [Text_Pipeline_AutoProcessing_Notebook.ipynb](sandbox:/mnt/data/Text_Pipeline_AutoProcessing_Notebook.ipynb)

Run all the cells and start processing files automatically!

### 3️⃣ **Watch for File Uploads**
- Place new files into the **`./uploads`** folder.
- The system **automatically detects and processes** them.

### 4️⃣ **Use Retrieval-Augmented Generation (RAG)**
- Once embeddings are stored, query them via the **RAG pipeline**.
- Ask AI-based questions against stored text.

### 5️⃣ **Store to Google Drive (Optional)**
- Authenticate with Google Drive to store processed files in the cloud.

---

## 🔍 Example Workflow
1. Upload a **PDF** to `./uploads`.
2. The pipeline extracts text, cleans it, and summarizes key points.
3. Chunks are created and **embedded** into FAISS/Pinecone.
4. The document is stored in **Google Drive**.
5. You can now **query the document** with AI-powered search.

---

## 🏗️ Future Enhancements
- **Streamlit UI** for a web interface.
- **API support** (FastAPI integration).
- **Multi-user cloud deployment**.

---

## 📝 Author & Contributions
Developed with ❤️ by AI-powered assistants. Contributions welcome!

---

## 📜 License
This project is open-source under the **MIT License**.
