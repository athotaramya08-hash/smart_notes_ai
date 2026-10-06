from utils.embeddings import (
    create_embeddings,
    create_question_embedding
)

from utils.rag import (
    create_vector_database,
    search_similar_chunks,
    generate_answer

)
from utils.rag import create_vector_database
from utils.embeddings import create_embeddings
from utils.summarizer import summarize_text
from utils.pdf_processor import extract_text_from_pdf
from utils.text_processor import clean_text, create_chunks
from utils.pdf_processor import extract_text_from_pdf
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="SmartNotes AI",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# CUSTOM CSS + HTML
# =========================================================

st.html("""
<style>

body {
    background-color: #0b1020;
}

.main-container {
    background: #0b1020;
    color: white;
    font-family: Arial, sans-serif;
}


/* ================= HEADER ================= */

.header {
    background: #11182d;
    border: 1px solid #293452;
    border-radius: 18px;

    padding: 18px 25px;

    display: flex;
    justify-content: space-between;
    align-items: center;

    margin-bottom: 45px;
}

.logo {
    font-size: 25px;
    font-weight: bold;
}

.logo-ai {
    color: #8b5cf6;
}

.status {
    background: #132c24;
    color: #4ade80;

    padding: 8px 15px;

    border-radius: 20px;

    font-size: 14px;

    border: 1px solid #24563f;
}


/* ================= HERO ================= */

.hero {
    text-align: center;

    padding: 35px 20px 50px;
}

.badge {
    display: inline-block;

    background: #19163b;

    border: 1px solid #40377d;

    color: #a78bfa;

    padding: 8px 18px;

    border-radius: 25px;

    font-size: 14px;

    margin-bottom: 20px;
}

.hero-title {
    font-size: 52px;

    font-weight: 700;

    margin: 10px 0 20px;

    line-height: 1.15;
}

.gradient {
    background: linear-gradient(
        90deg,
        #8b5cf6,
        #06b6d4
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

.hero-description {
    color: #9da7bd;

    font-size: 18px;

    max-width: 700px;

    margin: auto;

    line-height: 1.7;
}


/* ================= UPLOAD ================= */

.upload-box {
    max-width: 850px;

    margin: 0 auto 60px;

    padding: 35px;

    background: #11182d;

    border: 1px solid #303b5b;

    border-radius: 22px;

    text-align: center;

    box-shadow:
        0 15px 50px rgba(0,0,0,0.3);
}

.upload-title {
    font-size: 25px;

    font-weight: 600;

    margin-bottom: 10px;
}

.upload-description {
    color: #8f98ae;

    font-size: 15px;
}


/* ================= SECTION ================= */

.section-title {
    text-align: center;

    font-size: 32px;

    font-weight: 600;

    margin-top: 55px;

    margin-bottom: 10px;
}

.section-description {
    text-align: center;

    color: #8f98ae;

    margin-bottom: 35px;
}


/* ================= FEATURE CARDS ================= */

.card-container {
    display: flex;

    gap: 20px;

    max-width: 1100px;

    margin: auto;
}

.feature-card {
    flex: 1;

    background: #11182d;

    border: 1px solid #293452;

    border-radius: 20px;

    padding: 28px;

    min-height: 180px;

    transition: all 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-6px);

    border-color: #725cff;

    box-shadow:
        0 15px 40px rgba(0,0,0,0.3);
}

.feature-icon {
    font-size: 34px;

    margin-bottom: 15px;
}

.feature-title {
    font-size: 19px;

    font-weight: 600;

    margin-bottom: 10px;
}

.feature-description {
    color: #8f98ae;

    font-size: 14px;

    line-height: 1.6;
}


/* ================= STEPS ================= */

.steps {
    display: flex;

    gap: 20px;

    max-width: 1100px;

    margin: auto;
}

.step {
    flex: 1;

    text-align: center;

    padding: 25px;
}

.number {
    width: 50px;

    height: 50px;

    border-radius: 50%;

    background: #211c4a;

    border: 1px solid #51449b;

    color: #a78bfa;

    display: flex;

    align-items: center;

    justify-content: center;

    margin: 0 auto 15px;

    font-size: 20px;

    font-weight: bold;
}

.step-title {
    font-size: 17px;

    font-weight: 600;

    margin-bottom: 8px;
}

.step-description {
    color: #8f98ae;

    font-size: 14px;
}


/* ================= FOOTER ================= */

.footer {
    text-align: center;

    color: #69738a;

    margin-top: 70px;

    padding: 25px;

    border-top: 1px solid #222b42;
}

</style>


<div class="main-container">


    <!-- HEADER -->

    <div class="header">

        <div class="logo">
            🧠 SmartNotes <span class="logo-ai">AI</span>
        </div>

        <div class="status">
            ● AI System Ready
        </div>

    </div>


    <!-- HERO -->

    <div class="hero">

        <div class="badge">
            ✨ AI-Powered Study Assistant
        </div>

        <div class="hero-title">

            Turn Your Notes Into

            <span class="gradient">
                Smart Knowledge
            </span>

        </div>

        <div class="hero-description">

            Upload your study material and let SmartNotes AI
            summarize, understand and answer questions
            from your notes.

        </div>

    </div>


    <!-- UPLOAD BOX -->

    <div class="upload-box">

        <div class="upload-title">
            📚 Upload Your Study Material
        </div>

        <div class="upload-description">
            Upload a PDF and start learning smarter.
        </div>

    </div>


    <!-- FEATURES -->

    <div class="section-title">
        Everything You Need To Study Smarter
    </div>

    <div class="section-description">
        Powerful AI capabilities designed for students.
    </div>


    <div class="card-container">


        <div class="feature-card">

            <div class="feature-icon">
                📄
            </div>

            <div class="feature-title">
                PDF Understanding
            </div>

            <div class="feature-description">
                Upload your study material and extract
                important content automatically.
            </div>

        </div>


        <div class="feature-card">

            <div class="feature-icon">
                ✨
            </div>

            <div class="feature-title">
                AI Summarization
            </div>

            <div class="feature-description">
                Convert long study material into
                simple and useful summaries.
            </div>

        </div>


        <div class="feature-card">

            <div class="feature-icon">
                💬
            </div>

            <div class="feature-title">
                Ask Questions
            </div>

            <div class="feature-description">
                Ask questions about your notes and
                get answers from your study material.
            </div>

        </div>


    </div>


    <!-- HOW IT WORKS -->

    <div class="section-title">
        How SmartNotes AI Works
    </div>

    <div class="section-description">
        From your PDF to intelligent answers in four simple steps.
    </div>


    <div class="steps">


        <div class="step">

            <div class="number">
                1
            </div>

            <div class="step-title">
                Upload
            </div>

            <div class="step-description">
                Upload your PDF study material.
            </div>

        </div>


        <div class="step">

            <div class="number">
                2
            </div>

            <div class="step-title">
                Process
            </div>

            <div class="step-description">
                Extract and prepare the document.
            </div>

        </div>


        <div class="step">

            <div class="number">
                3
            </div>

            <div class="step-title">
                Understand
            </div>

            <div class="step-description">
                AI understands the important content.
            </div>

        </div>


        <div class="step">

            <div class="number">
                4
            </div>

            <div class="step-title">
                Learn
            </div>

            <div class="step-description">
                Ask questions and get useful answers.
            </div>

        </div>


    </div>


    <!-- FOOTER -->

    <div class="footer">

        🧠 SmartNotes AI

        <br>

        Your intelligent study companion

    </div>


</div>
""")


# =========================================================
# PDF UPLOADER
# =========================================================

st.markdown("### 📄 Upload Your PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)


# =========================================================
# UPLOAD RESULT
# =========================================================
if uploaded_file is not None:

    # ==============================
    # 1. File Upload Success
    # ==============================

    st.success(
        f"✅ {uploaded_file.name} uploaded successfully!"
    )


    # ==============================
    # 2. Extract Text from PDF
    # ==============================

    text = extract_text_from_pdf(uploaded_file)


    # ==============================
    # 3. Clean Extracted Text
    # ==============================

    cleaned_text = clean_text(text)


    # ==============================
    # 4. Create Text Chunks
    # ==============================

    chunks = create_chunks(cleaned_text)


    # ==============================
    # 5. Create Embeddings
    # ==============================

    embeddings = create_embeddings(chunks)
    collection = create_vector_database(
    chunks,
    embeddings,
    uploaded_file.name
)
    # ==============================
    # 6. Display Extracted Text
    # ==============================

    st.subheader("📄 Extracted Text")

    st.text_area(
        "PDF Content",
        cleaned_text,
        height=300
    )


    # ==============================
    # 7. Display Text Chunks
    # ==============================

    st.subheader("🧩 Text Chunks")

    st.write(
        f"Total chunks created: {len(chunks)}"
    )

    for i, chunk in enumerate(chunks[:3]):

        st.write(f"### Chunk {i + 1}")

        st.write(chunk)


    # ==============================
    # 8. Display Embeddings
    # ==============================

    st.subheader("🔢 Embeddings")

    st.write(
        f"Created embeddings for {len(embeddings)} chunks."
    )

    st.write(
        "Embedding dimensions:",
        embeddings.shape
    )


    # ==============================
    # 9. AI Summary
    # ==============================

    st.subheader("✨ AI Summary")

    if st.button("Generate Summary"):

        with st.spinner(
            "🤖 AI is reading your notes..."
        ):

            summary = summarize_text(chunks[0])


        st.success(
            "Summary generated!"
        )

        st.write(summary)
# ==============================
# 10. Ask Questions
# ==============================

st.subheader("💬 Ask Your Notes")

question = st.text_input(
    "Ask a question about your PDF"
)

if st.button("🤖 Ask SmartNotes AI"):

    if question:

        with st.spinner(
            "🔎 Searching your notes..."
        ):

            # Step 1: Convert question into embedding
            question_embedding = create_question_embedding(
                question
            )

            # Step 2: Search ChromaDB
            results = search_similar_chunks(
                collection,
                question_embedding,
                n_results=3
            )

            # Step 3: Get relevant documents
            relevant_chunks = results["documents"][0]

            # Step 4: Combine chunks into context
            context = "\n\n".join(
                relevant_chunks
            )

        with st.spinner(
            "🤖 Generating answer..."
        ):

            # Step 5: Ask LLM
            answer = generate_answer(
                question,
                context
            )

        # Step 6: Display answer
        st.success("Answer generated!")

        st.write("### 🧠 AI Answer")

        st.write(answer)

    else:

        st.warning(
            "Please enter a question."
        )