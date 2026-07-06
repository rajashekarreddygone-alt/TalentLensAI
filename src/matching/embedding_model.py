from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def get_embedding(text: str):
    """
    Convert text into a semantic embedding.
    """
    return model.encode(text)