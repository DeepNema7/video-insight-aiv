import streamlit as st
import requests

st.set_page_config(page_title="Video Insight AI", layout="wide")

st.title("🎥 Video Insight AI")
st.write("Upload video and get insights")

video = st.file_uploader("Upload Video", type=["mp4", "mov"])

if video:
    st.video(video)

    if st.button("Generate Insights 🚀"):
        with st.spinner("Processing..."):
            files = {"file": video}
            res = requests.post("http://127.0.0.1:8000/process", files=files)
            data = res.json()

        st.success("Done!")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📄 Summary")
            st.write(data["summary"])

        with col2:
            st.subheader("🏷️ Topics")
            st.write(data["topics"])

        st.subheader("⏱️ Key Moments")
        for t in data["timestamps"]:
            st.write(f"{t['time']} - {t['text']}")

st.subheader("💬 Chat with Video")

query = st.text_input("Ask something")

if query:
    res = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"query": query}
    )
    st.write(res.json()["answer"])