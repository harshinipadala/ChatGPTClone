import streamlit as st

st.title("EchoBot")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Old Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Response
if prompt := st.chat_input("Message EchoBot"):
    # Display the user's message
    st.chat_message("user").markdown(prompt)
    # Add their message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display the response
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add response to history
    st.session_state.messages.append({"role": "assistant", "content": response})