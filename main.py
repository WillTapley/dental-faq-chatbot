from fastapi import FastAPI, Request
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful FAQ assistant for a dental clinic."},
            {"role": "user", "content": user_input}
        ]
    )
    return {"response": response['choices'][0]['message']['content']}
