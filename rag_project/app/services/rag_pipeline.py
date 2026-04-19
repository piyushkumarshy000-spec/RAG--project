from app.core.retriever import retrieve
from app.core.reranker import rerank
from app.core.llm import generate_answer

def run_rag(query):
    # Step 1: Retrieve
    chunks = retrieve(query, k=10)

    # Step 2: Rerank
    best_chunks = rerank(query, chunks, top_k=3)

    # Step 3: Build context
    context = "\n".join([c["text"] for c in best_chunks])

    # Step 4: Generate answer
    answer = generate_answer(context, query)

    # Step 5: Extract sources
    sources = [
        f"{c['source']} (chunk {c['id']})"
        for c in best_chunks
    ]

    return {
        "answer": answer,
        "sources": sources
    }