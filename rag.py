import chromadb
import ollama


def create_vector_database(chunks, embeddings, document_name):

    client = chromadb.PersistentClient(
        path="data/chroma_db"
    )

    collection = client.get_or_create_collection(
        name="smart_notes"
    )

    # Create unique IDs for this document
    ids = [
        f"{document_name}_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=[
            {
                "source": document_name,
                "chunk": i
            }
            for i in range(len(chunks))
        ]
    )

    return collection


def search_similar_chunks(
    collection,
    question_embedding,
    n_results=3
):

    results = collection.query(
        query_embeddings=[
            question_embedding.tolist()
        ],
        n_results=n_results
    )

    return results


def generate_answer(question, context):

    prompt = f"""
You are SmartNotes AI, an educational assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not available in the context,
say:

"I couldn't find the answer in your notes."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]