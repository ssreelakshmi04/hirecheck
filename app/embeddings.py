from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')


def generate_embeddings(text):
    """Generates embeddings for a given text."""
    return model.encode([text])[0]


def calculate_similarity(embedding1, embedding2):
    """Calculates cosine similarity between two embeddings."""
    similarity = cosine_similarity([embedding1], [embedding2])
    return round(similarity[0][0] * 100, 2)
