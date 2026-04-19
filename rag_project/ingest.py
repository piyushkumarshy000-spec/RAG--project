from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Read file
with open("data/sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 🔥 SMART CHUNKING
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,        # max characters per chunk
    chunk_overlap=20,      # overlap between chunks
    separators=["\n\n", "\n", ".", " ", ""]
)

chunks = text_splitter.split_text(text)

print(f"Total chunks created: {len(chunks)}")

# Create embeddings
embeddings = model.encode(chunks)
embeddings = np.array(embeddings).astype('float32')

# Store in FAISS
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "faiss_index.bin")

with open("chunks.npy", "wb") as f:
    chunk_data = [
    {
        "text": chunk,
        "source": "sample.txt",
        "id": i
    }
    for i, chunk in enumerate(chunks)
]

np.save("chunks.npy", chunk_data)

print("✅ Smart ingestion done")