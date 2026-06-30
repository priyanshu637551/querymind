import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)
SCHEMA = """
customers(
    customer_id,
    first_name,
    last_name,
    gender,
    age_group,
    signup_date,
    country
)
products(
    product_id,
    product_name,
    category,
    unit_price
)
orders(
    order_id,
    customer_id,
    product_id,
    quantity,
    order_date,
    order_status,
    payment_method
)
reviews(
    review_id,
    customer_id,
    product_id,
    rating,
    review_text,
    review_date
)
"""


def generate_sql(question):
    prompt = f"""
    You are a PostgreSQL expert.
    Database schema:
    {SCHEMA}
    Convert the user's question into PostgreSQL SQL.
    Rules:
    1. Return ONLY SQL.
    2. No explanation.
    3. No markdown.
    4. Use only tables and columns from schema.
    Question:
    {question}
    """
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

def fix_sql(question, bad_sql, error_message):
    prompt = f"""
    You are a PostgreSQL expert.
    Database schema:
    {SCHEMA}
    The following SQL failed.
    Question:
    {question}
    Bad SQL:
    {bad_sql}
    PostgreSQL Error:
    {error_message}
    Fix the SQL.
    Return ONLY SQL.
    """