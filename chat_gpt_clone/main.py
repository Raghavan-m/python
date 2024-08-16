import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq 

# Load environment variables
load_dotenv()

# system configuration

temp =0
context_size = 8000
system_prompt = "you are helpfull assistant"
model_name  = "llama-3.1-70b-versatile"

#api key from env
groq_api = os.getenv('groq_api_key')

# Streamlit page configuration
st.set_page_config(
    page_title="Groq-Llama 3.1-70B",
    page_icon="🤖",
    layout="centered"
)

# Title of the Streamlit app
st.title('Groq-Llama 3.1-70B')

# Get user input from chat input
prompt = st.chat_input('Ask anything...')

# Initialize session state for chat history if not already present
if "chats" not in st.session_state:
    st.session_state.chats = []

# Process user prompt
if prompt:
    # Add user message to chat history
    st.session_state.chats.append({
        "role": "user",
        "content": prompt
    })

    # Initialize Groq client
    client = Groq(
        api_key=groq_api
    )

    # Create completion using the Groq client
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.chats,
            {"role": "user", "content": prompt}
        ],
        temperature=temp,
        max_tokens=context_size,
        top_p=1,
        stream=True,
        stop=None,
    )

    # Retrieve response from the completion stream
    response = ""
    for chunk in completion:
        if chunk.choices[0].delta:
            response += chunk.choices[0].delta.content or ""

    # Add assistant response to chat history
    st.session_state.chats.append({
        "role": "assistant",
        "content": response
    })

# Display chat messages
for chat in st.session_state.chats:
    st.chat_message(chat['role']).markdown(chat['content'])
