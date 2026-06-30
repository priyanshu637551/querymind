import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)
def generate_summary(question, columns, rows):

    prompt = f"""
    Question:{question}
    Columns:{columns}
    Data:{rows[:20]}
    Write a short business summary in 3-4 lines.
    Avoid technical language."""
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    return response.text.strip()