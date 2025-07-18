import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
load_dotenv()



MONGO_URI = os.getenv("MONGO_URI","mongodb+srv://mominarashad137:YHfYRbcr2FyyoWQB@cluster0.vsxvet0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


DB_NAME = "hybrid_retrieval"
COLLECTION_NAME = "issues"

HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL_ID = "sentence-transformers/paraphrase-MiniLM-L6-v2"
HF_MODEL_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}"
