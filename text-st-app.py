# pylint: disable=all
import streamlit as st
from openai import AzureOpenAI
import os
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Initialize Azure OpenAI with environment variables
client = AzureOpenAI(
    azure_endpoint=os.getenv("openai_api_endpoint"),
    azure_deployment=os.getenv("openai_completions_deployment"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY2"),
    api_version=os.getenv("openai_api_version")
)

# Fetch deployment and model
deployment = os.getenv('AZURE_OPENAI_DEPLOYMENT')

# Streamlit interface
st.title("Azure OpenAI Text Generation")

# Input field for the prompt
prompt = st.text_input("Enter a prompt:", value=" ")

# Button to generate text
if st.button("Generate Text"):
    if prompt:
        # Prepare the request
        messages = [{"role": "user", "content": prompt}]
        
        # Make the completion request
        with st.spinner('Generating...'):
            completion = client.chat.completions.create(model=deployment, messages=messages)
        
        # Display the response
        st.success("AI-generated response:")
        st.write(completion.choices[0].message.content)
    else:
        st.error("Please enter a prompt!")
