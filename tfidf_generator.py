from sklearn.feature_extraction.text import TfidfVectorizer

class TFIDFHandler:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.vectors = None

    def fit_transform(self, texts: list):
        self.vectors = self.vectorizer.fit_transform(texts)
        return self.vectors.toarray()

    def transform(self, text: str):
        return self.vectorizer.transform([text]).toarray()[0]
