from sentence_transformers import CrossEncoder

# 🔥 Cross-encoder model (very accurate)
reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank(query, chunks, top_k=3):
    # Pair query with each chunk
    pairs = [(query, chunk["text"]) for chunk in chunks]

    # Get relevance scores
    scores = reranker.predict(pairs)

    # Combine chunks + scores
    scored_chunks = list(zip(chunks, scores))

    # Sort by score (highest first)
    scored_chunks.sort(key=lambda x: x[1], reverse=True)

    # Return top_k chunks
    top_chunks = [chunk for chunk, score in scored_chunks[:top_k]]

    return top_chunks