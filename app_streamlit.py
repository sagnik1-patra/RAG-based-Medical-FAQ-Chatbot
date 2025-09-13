import streamlit as st
from src.retriever import retrieve
from src.generator import answer

st.set_page_config(page_title="Medical FAQ RAG Bot", page_icon="🩺")
st.title("🩺 Medical FAQ Chatbot (RAG)")
st.caption("Answers are grounded in your FAQ dataset")

q = st.text_input("Ask a medical question...")

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Ask") and q.strip():
    hits = retrieve(q)
    ans = answer(q, hits)
    st.session_state.history.append((q, ans, hits))

for (qq, aa, hh) in reversed(st.session_state.history):
    st.markdown(f"**You:** {qq}")
    st.markdown(f"**Bot:** {aa}")
    with st.expander("Show retrieved context"):
        for h in hh:
            st.markdown(f"- {h['meta'].get('source','faq')} (score={h['score']:.3f})")
            st.markdown(f"  {h['text']}")
    st.markdown("---")
