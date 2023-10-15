import os 
import openai
from dotenv import load_dotenv

load_dotenv(".env")

openai.api_key = os.getenv("API_KEY_OPENIA")

while True:
    prompt = input("\n Igresa tu pregunta: ")
    
    if prompt == "salir":
        break
    
    completion = openai.Completion.create(
        engine = "text-davinci-003", prompt = prompt, max_tokens=2048
    )
    print(completion.choices[0].text)