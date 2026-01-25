from sklearn.feature_extraction.text import TfidfVectorizer

def build_index(chunks):
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(chunks)
    return {"chunks": chunks, "matrix": matrix}
