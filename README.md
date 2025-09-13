# 🩺 RAG Medical FAQ Chatbot

This is a Retrieval-Augmented Generation (RAG) chatbot for medical FAQs.

## Setup
```bash
pip install -r requirements.txt
```
Copy `.env.example` to `.env` and add your OpenAI API key.

## Ingest Data
```bash
python -m src.ingest
```

## Run Chatbot
### Streamlit UI
```bash
streamlit run app_streamlit.py
```
### CLI
```bash
python cli.py "What are early symptoms of diabetes?"
```

⚠️ Disclaimer: For educational/demo use only. Not medical advice.
