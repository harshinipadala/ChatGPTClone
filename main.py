import streamlit as st
import random
import time

# Pre-determined responses
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi! Is there anything I can help you with?",
            "What can I help you with?",
        ]
    )
    # slows down the responses
    for word in response.split(): 
        yield word + " "
        time.sleep(0.05)

st.title("Simple Chatbot GUI")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Old Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Response
if prompt := st.chat_input("Message Simple Bot"):
    # Add their message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display the user's message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant's response
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())

    #Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})



