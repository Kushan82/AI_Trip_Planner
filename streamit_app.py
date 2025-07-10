import streamlit as st
import datetime
import requests
import sys

BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title=" Travel Butler Ai Agent",
    page_icon="🛫 ",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.title("🤵‍♂️Travel Butler Ai Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("How can I help you,Let me know where you want to vist")

with st.form(key="query_form",clear_on_submit=True):
    user_input = st.text_input("User Input", placeholder="plan a trip for ...")
    submit_button =st.form_submit_button("Send")

if submit_button and user_input.strip():
    try:
        with st.spinner("Thinking..."):
            payload = {"question":user_input}
            response = requests.post(f"{BASE_URL}/query",json= payload)

        if response.status_code == 200:
            answer = response.json().get("answer","no answer returned")
            markdown_content = f""" # AI TRAVEL PLAN
            ---
            {answer}
            ---
            *Ai generated plan """
            st.markdown(markdown_content)
        else: 
            st.error("Failed to respond:"+ response.text)
    except Exception as e:
        raise f"The response failed due to {e}"