# bm25_handler.py
from langchain.retrievers import BM25Retriever
from langchain.schema import Document

class BM25Handler:
    def __init__(self, texts: list[str]):
        self.docs = [Document(page_content=txt) for txt in texts]
        self.retriever = BM25Retriever.from_documents(self.docs)

    def get_scores(self, query: str) -> list[float]:
        top_docs = self.retriever.get_relevant_documents(query)
        top_texts = [doc.page_content for doc in top_docs]

        scores = []
        for doc in self.docs:
            # Score is inversely proportional to rank
            if doc.page_content in top_texts:
                rank = top_texts.index(doc.page_content)
                score = 1 / (rank + 1)
            else:
                score = 0
            scores.append(score)
        return scores
