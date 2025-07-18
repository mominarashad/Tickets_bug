---
title: Tickets Issue Search (MCP)
emoji: 🧠
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 8000
sdk_version: 1.0.0
mcp_server: true
license: mit
---

# 🎫 Tickets Issue Search (Hybrid RAG Tool)

A FastAPI-based hybrid retrieval tool using BM25 + Embedding search, connected to MongoDB, built for issue resolution.

## ✅ MCP Tool Support

This app supports [MCP](https://huggingface.co/docs/hub/spaces-mcp-servers) and exposes:

- `/invocations`: Main inference endpoint
- `/metadata`: Tool metadata for LLMs
- `/healthz`: Health check

## 📦 How to Query

```bash
curl -X POST https://your-space-url.hf.space/invocations \
  -H "Content-Type: application/json" \
  -d '{"inputs": "Why is data not syncing in dashboard?"}'
```
---
## 📁 Project Structure

```bash
Tickets/
├── bm25_handler.py          # BM25-based text retriever
├── config.py                # Configuration constants (optional)
├── data_loader.py           # Excel reading and preprocessing logic
├── embedding_generator.py   # Embedding generator for input text
├── main.py                  # FastAPI entrypoint with endpoints
├── mcp_processor.py         # Context extraction from Excel rows
├── mongo_store.py           # MongoDB insert/retrieve logic
├── retriever.py             # Hybrid BM25 + embedding search logic
├── tfidf_generator.py       # (Optional) TF-IDF generator (if used)
├── ultra_refined_descriptions.xlsx # Input data (ignored in Git)
├── .env                     # API keys or secrets (ignored by Git)
├── .gitignore               # Ignore rules for Git
└── requirements.txt         # Python dependencies
```

---

## 🚀 Features

- 🧪 **BM25 keyword search** using LangChain's `BM25Retriever`
- 🧠 **Semantic search** using embedding vectors
- 🔍 **Hybrid ranking** for higher precision
- 🗂 **MongoDB storage** for persistent issue data
- 📄 Accepts Excel files as the primary input
- ⚡ Powered by FastAPI with clean, async-ready architecture

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mominarashad/Tickets.git
cd Tickets
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install the requirements

```bash
pip install -r requirements.txt
```

### 4. Prepare your `.env` file

Create a `.env` file in the root with your keys (e.g., Hugging Face key):

```
HUGGINGFACE_API_TOKEN=your_token_here
```

**Do not commit this file** (already ignored in `.gitignore`).

---

## 📄 Input File

The system expects an Excel file named:

```
ultra_refined_descriptions.xlsx
```

It should be placed in the root directory and must contain the required fields like `description`, `title`, etc. (based on your `extract_context` logic in `mcp_processor.py`).

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Then visit:

```
http://127.0.0.1:8000/docs
```

Here, you can test the `/search/` endpoint with your query.

---

## 🔍 Search Endpoint

### `GET /search/`

**Query Parameter**:  
`query` (string): The search text to match against stored issues.

**Example**:

```http
GET /search/?query=payment delay issue
```

Returns a list of the most relevant issues ranked by hybrid BM25 + embedding score.

---

## 🧪 Example Code Usage

To search from your Python script:

```python
import requests

query = "data mismatch error"
response = requests.get("http://127.0.0.1:8000/search/", params={"query": query})

print(response.json())
```


---

## 🛡️ Security Notes

- Secrets are stored in `.env` (make sure it's in `.gitignore`)
- Avoid uploading `.env`, `.xlsx`, or token files to GitHub

---


## 🙌 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Hugging Face](https://huggingface.co/)
