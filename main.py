import streamlit as st
from openai import OpenAI


st.title("ChatGPT clone")

st.sidebar.subheader("About")
st.sidebar.markdown("""
This is a ChatGPT clone built using Streamlit and OpenAI's GPT-3.5. It allows for interactive chatting with an AI assistant. """)
st.sidebar.markdown("---")

st.sidebar.markdown(" ")
api_key = st.text_input("Enter your OpenAI API key to begin:")
client = OpenAI(api_key=api_key)

uploaded_file = st.sidebar.file_uploader("# Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Read the PDF file
    pdf_reader = PdfFileReader(uploaded_file)
    num_pages = pdf_reader.getNumPages()

    # Display the number of pages
    st.write(f"Number of pages in the PDF: {num_pages}")

    # Display each page of the PDF
    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        page_text = page.extractText()
        st.write(f"Page {page_num + 1}:")
        st.write(page_text)
else:
    st.sidebar.info("#### Upload a PDF file using the file uploader above.")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})



st.sidebar.markdown("---")
st.sidebar.markdown(" ")

st.sidebar.markdown("Created by Harshini Padala")
st.sidebar.markdown("Powered by Streamlit and OpenAI")
