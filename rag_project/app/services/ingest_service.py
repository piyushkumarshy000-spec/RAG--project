from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
import faiss
import numpy as np
from pypdf import PdfReader
import os

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_or_create_index(dim=384):
    if os.path.exists("faiss_index.bin"):
        index = faiss.read_index("faiss_index.bin")
        chunk_data = list(np.load("chunks.npy", allow_pickle=True))
    else:
        index = faiss.IndexFlatL2(dim)
        chunk_data = []
    return index, chunk_data


def process_file(file_path, filename):
    text = ""

    # ✅ HANDLE PDF
    if filename.lower().endswith(".pdf"):
        reader = PdfReader(file_path)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    # ✅ HANDLE TXT
    elif filename.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    else:
        raise ValueError("Unsupported file type (only PDF/TXT allowed)")

    # 🚨 IMPORTANT CHECK
    if not text.strip():
        raise ValueError("No readable text found in file")

    # ✅ Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=150,
        chunk_overlap=30
    )
    chunks = splitter.split_text(text)

    # Load index
    index, chunk_data = load_or_create_index()

    # Embeddings
    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype('float32')

    index.add(embeddings)

    # Add metadata
    start_id = len(chunk_data)
    for i, chunk in enumerate(chunks):
        chunk_data.append({
            "text": chunk,
            "source": filename,
            "id": start_id + i
        })

    # Save
    faiss.write_index(index, "faiss_index.bin")
    np.save("chunks.npy", chunk_data)

    return len(chunks)