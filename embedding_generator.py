from sentence_transformers import SentenceTransformer

# Load the embedding model once
model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L6-v2")

def generate_embedding(text: str) -> list:
    """
    Generate embedding for a single string input using a local model.
    """
    return model.encode(text).tolist()
