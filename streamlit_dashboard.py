import streamlit as st
import os
import glob

st.set_page_config(page_title="📊 AI Text Pipeline Dashboard", layout="wide")

st.title("📊 AI Text Processing Dashboard")
st.markdown("Monitor uploaded files, summaries, and logs in real-time.")

# Directory to monitor
UPLOAD_DIR = "data/uploads"
PROCESSED_DIR = "data/processed"

st.header("📂 Uploaded Files")
uploaded_files = glob.glob(os.path.join(UPLOAD_DIR, "*"))
if uploaded_files:
    for file in uploaded_files:
        st.write(f"📄 {os.path.basename(file)}")
else:
    st.info("No files uploaded yet.")

st.header("✅ Processed Files")
processed_files = glob.glob(os.path.join(PROCESSED_DIR, "*"))
if processed_files:
    for file in processed_files:
        st.write(f"📦 {os.path.basename(file)}")
else:
    st.info("No processed files available.")

st.header("🧠 Summaries")
summary_logs = glob.glob("*.summary.txt")
if summary_logs:
    for log in summary_logs:
        st.subheader(f"📝 {os.path.basename(log)}")
        with open(log, "r", encoding="utf-8") as f:
            st.code(f.read(), language="markdown")
else:
    st.warning("No summaries generated yet.")
