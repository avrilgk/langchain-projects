from langchain.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY3")

# Initialize the ChatOpenAI model with the API key
chat_model = ChatOpenAI(openai_api_key=api_key)

def generate_pet_names():
    llm = OpenAI(temperature=0)

    name = llm("I have a pet dog and I want a cool name for it. Suggest 4 names")

    return name
    
if __name__ == "__main__": 
    print(generate_pet_names())
