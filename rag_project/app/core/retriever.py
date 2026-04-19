import faiss
import numpy as np
from app.core.embeddings import get_embedding

index = faiss.read_index("faiss_index.bin")
chunk_data = np.load("chunks.npy", allow_pickle=True)

def retrieve(query, k=10):
    query_embedding = get_embedding(query)
    distances, indices = index.search(query_embedding, k)

    results = [chunk_data[i] for i in indices[0]]
    return results