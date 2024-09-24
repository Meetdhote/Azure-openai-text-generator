# pylint: disable=all
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

# Define the prompt
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]  

# Make the completion request
completion = client.chat.completions.create(model=deployment, messages=messages)

# Print the response
print(completion.choices[0].message.content)
