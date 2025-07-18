# main.py
from fastapi import FastAPI
from data_loader import load_and_prepare
from mcp_processor import extract_context
from embedding_generator import generate_embedding
from mongo_store import store_issue, get_all_issues
from retriever import hybrid_search
from bm25_handler import BM25Handler
from fastapi.responses import JSONResponse

FILE_PATH = "ultra_refined_descriptions.xlsx"

app = FastAPI()
bm25_handler = None
all_issues = []

@app.on_event("startup")
def process_excel_on_start():
    global bm25_handler, all_issues

    df = load_and_prepare(FILE_PATH)
    contexts = []

    for _, row in df.iterrows():
        ctx = extract_context(row)
        ctx["embedding_vector"] = generate_embedding(ctx["full_text"])
        contexts.append(ctx)

    for ctx in contexts:
        store_issue(ctx)

    all_issues = contexts
    bm25_handler = BM25Handler([c["full_text"] for c in contexts])

    print(f"{len(contexts)} rows processed and stored.")

@app.get("/search/")
def search_issue(query: str):
    if not bm25_handler or not all_issues:
        return {"error": "System not initialized"}

    results = hybrid_search(query, bm25_handler, all_issues)

    # Remove _id fields if present (Mongo adds them during storage)
    cleaned = []
    for item in results:
        item = dict(item)
        item.pop("_id", None)  # safely remove if exists
        cleaned.append(item)

    return JSONResponse(content=cleaned)
