import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


def gemini(input):
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(input)

    return response.text
