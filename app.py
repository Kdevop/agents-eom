import streamlit as st
import requests
import uuid

st.title("UPlan — Your Event Finder")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Display chat history using chat bubbles
for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]

    if role == "user":
        with st.chat_message("user"):
            st.markdown(content)
    else:
        with st.chat_message("assistant"):
            st.markdown(content)

# User input (Enter to send)
user_input = st.chat_input("Your message")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    payload = {
        "sessionId": st.session_state.session_id,
        "message": user_input,
    }

    response = requests.post(
        "https://kiernanhall.app.n8n.cloud/webhook/uplan",
        json=payload
    )

    try:
        assistant_reply = response.json()
    except:
        assistant_reply = {"response": response.text}

    assistant_text = assistant_reply.get("response", response.text)

    # Add assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_text
    })

    st.rerun()