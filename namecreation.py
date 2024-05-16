# Application is WIP. 

import warnings
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# Suppress the LangChainDeprecationWarning warning for deprecated method usage
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain_core")

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY2")

# Initialize the ChatOpenAI model with the API key
chat_model = ChatOpenAI(openai_api_key=api_key)


response = chat_model.invoke("I want to open a Chinese restaurant in New York City. What should I name it?")
print(response.content)