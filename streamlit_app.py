import streamlit as st
import os

st.set_page_config(page_title="AI Text Pipeline", layout="centered")

st.title("🧠 AI Text Processing Pipeline")
st.markdown("Upload a `.txt`, `.pdf`, or `.docx` file to process it with summarization and embeddings.")

uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"])

if uploaded_file:
    file_path = os.path.join("data/uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File uploaded to {file_path}.")
    st.info("🕒 Please wait — file will be auto-processed in background.")
