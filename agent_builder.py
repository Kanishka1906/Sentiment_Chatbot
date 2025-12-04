from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()  

def build_agent():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Check your .env file.")

    return Groq(api_key=api_key)
