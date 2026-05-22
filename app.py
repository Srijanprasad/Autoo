import os
import streamlit as st
import requests

WEBHOOK_URL = st.secrets.get("WEBHOOK_URL") or os.getenv("WEBHOOK_URL", "")

st.title("🤝 Your Personal Assistant")
st.subheader("What can your personal assistant do?")

st.markdown(
    """
    1. Answer questions on various topics.
    2. Arrange calendar events and meetings.
    3. Read your emails and send replies, can even summarize them for you.
    4. Manage your tasks and to-do lists.
    5. Take quick notes for you.
    6. Track your expenses and budgeting.
    """
)

st.subheader("💬 Chat with your assistant")
st.caption(f"Using webhook: {WEBHOOK_URL or 'not configured'}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Send a message")

if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

    if not WEBHOOK_URL:
        st.error("Webhook URL is not configured. Set WEBHOOK_URL in Streamlit secrets or environment variables.")
    else:
        try:
            response = requests.post(WEBHOOK_URL, json={"message": user_message}, timeout=20)
            response.raise_for_status()
            payload = response.json()
            ai_response = payload[0].get("output") if isinstance(payload, list) else payload.get("output")
            if not ai_response:
                raise ValueError("Missing output field in webhook response")

        except Exception as exc:
            st.error(f"Error calling webhook: {exc}")
            ai_response = "Sorry, I could not reach the webhook."

        with st.chat_message("assistant"):
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})