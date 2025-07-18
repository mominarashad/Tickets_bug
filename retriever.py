# retriever.py
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from embedding_generator import generate_embedding

def hybrid_search(query: str, bm25_handler, issues, top_k=3):
    query_emb = generate_embedding(query)

    bm25_scores = bm25_handler.get_scores(query)

    max_bm25 = max(bm25_scores) if max(bm25_scores) != 0 else 1.0
    normalized_bm25_scores = [s / max_bm25 for s in bm25_scores]

    scores = []
    for idx, issue in enumerate(issues):
        emb_score = cosine_similarity([query_emb], [issue["embedding_vector"]])[0][0]
        bm25_score = normalized_bm25_scores[idx]
        hybrid_score = (emb_score + bm25_score) / 2
        scores.append((hybrid_score, issue))

    scores.sort(key=lambda x: x[0], reverse=True)
    return [item for _, item in scores[:top_k]]
