from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import streamlit as st


@st.cache_resource
def load_summarizer():

    model_name = "sshleifer/distilbart-cnn-12-6"

    tokenizer = AutoTokenizer.from_pretrained(
        model_name
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name
    )

    return tokenizer, model


def summarize_text(text):

    tokenizer, model = load_summarizer()

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=150,
        min_length=40,
        num_beams=4,
        early_stopping=True
    )

    summary = tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )

    return summary