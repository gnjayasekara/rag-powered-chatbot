from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()

context = "The interest rates for fixed deposits at DFCC Bank are higher for longer terms."
question = "What is the interest rate for a 6-month fixed deposit?"
prompt = f"Answer this question: {question}\nUsing only this context:\n{context}"

print(generate_response(prompt))