# Text-Generation-Apps


## Azure OpenAI Chat Completion Example

This project demonstrates how to use the Azure OpenAI service to generate text completions using both a chat-based approach and a Streamlit web application. The examples initialize an Azure OpenAI client, send a prompt, and display the generated response either in the console or through a web interface.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example Prompt](#example-prompt)
- [License](#license)

## Prerequisites

To run this project, ensure you have the following:

- Python 3.7 or higher
- An Azure account with access to Azure OpenAI
- An OpenAI API key and an Azure OpenAI API key

## Installation

1. Clone this repository to your local machine:
   git clone <repository-url>
   cd <repository-directory>

2. Install the required Python packages:
- pip install openai python-dotenv streamlit


## Environment Variables
Create a .env file in the project directory and add the following variables:

# OpenAI Provider
OPENAI_API_KEY='<add your OpenAI API key here>'

# Azure OpenAI
AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
AZURE_OPENAI_API_KEY='<add your Azure OpenAI key here>'
AZURE_OPENAI_ENDPOINT='<add your Azure OpenAI service endpoint here>'
AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

# Hugging Face
HUGGING_FACE_API_KEY='<add your Hugging Face API or token here>'

Replace the placeholder values with your actual API keys and endpoint information.

## Usage
Console Application
To run the console example, use the following command in your terminal:
- python <your_console_script_name.py>
This will initialize the Azure OpenAI client, send a prompt to the chat model, and print the completion generated by the model.

Streamlit Application
To run the Streamlit web application, use the following command in your terminal:
- streamlit run <your_streamlit_script_name.py>
This will open a web interface where you can enter a prompt and generate text using the Azure OpenAI service.

## Code Explanation
Code Explanation
The code provided in this project does the following:

- Imports Required Libraries: It imports the necessary libraries, including AzureOpenAI for accessing Azure OpenAI services, dotenv for loading environment variables, and streamlit for building the web interface.
- Loads Environment Variables: The dotenv.load_dotenv() function loads the environment variables from the .env file.
- Initializes Azure OpenAI Client: An instance of AzureOpenAI is created using the endpoint, deployment, API key, and version specified in the environment variables.
- Defines the Prompt: A prompt is defined to initiate the chat completion request.
- Sends Completion Request: The client sends a request to the Azure OpenAI service and retrieves the completion response.
- Prints or Displays the Response:
- - In the console application, the content of the response is printed to the console.
- - In the Streamlit application, the generated response is displayed in the web interface.

## Example Prompt
The example uses the following prompt to generate text:
prompt = "Complete the following: Once upon a time there was a"
- You can modify this prompt in the code to generate different completions or explore other use cases.


