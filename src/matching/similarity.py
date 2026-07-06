from sklearn.metrics.pairwise import cosine_similarity

from src.matching.embedding_model import get_embedding


def calculate_similarity(text1: str, text2: str):

    embedding1 = get_embedding(text1)

    embedding2 = get_embedding(text2)

    score = cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return round(float(score), 4)