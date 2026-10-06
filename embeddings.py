from sentence_transformers import SentenceTransformer
import streamlit as st


@st.cache_resource
def load_embedding_model():

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    return model


def create_embeddings(chunks):

    model = load_embedding_model()

    embeddings = model.encode(chunks)

    return embeddings


def create_question_embedding(question):

    model = load_embedding_model()

    embedding = model.encode(question)

    return embedding