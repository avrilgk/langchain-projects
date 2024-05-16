import warnings
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# Suppress the LangChainDeprecationWarning warning
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain_core")

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the ChatOpenAI model with the API key
chat_model = ChatOpenAI(openai_api_key=api_key)

# Define the template for the translation task
template = "You are a helpful assistant that translates {input} to {output}."
human_template = "{text}"

# Create the chat prompt template
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

while True:
    # Get the English text to be translated from the user
    english_text = input("\nEnter the English text to translate (or type 'exit' to quit): ")
    
    if english_text.lower() == 'exit':
        break

    # Get the target language from the user
    target_language = input("Enter the target language: ")

    # Format the messages for the chat model
    formatted_messages = chat_prompt.format_messages(
        input="English",
        output=target_language,
        text=english_text
    )

    # Ensure messages is a list of BaseMessage objects
    # The format_messages method should be returning BaseMessage objects already
    if not all(isinstance(msg, (SystemMessage, HumanMessage)) for msg in formatted_messages):
        raise ValueError("Formatted messages are not of the correct type")

    try:
        # Get the translation result
        result = chat_model.invoke(formatted_messages)

        # Print the translated content
        print("\nTranslated text:", result.content)
    except Exception as e:
        print(f"An error occurred: {e}")

print("Translation session ended.")
