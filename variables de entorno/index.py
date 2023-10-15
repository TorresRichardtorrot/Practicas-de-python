import os 
from dotenv import load_dotenv

load_dotenv(".env.dev")

user_name = os.getenv("USER_NAME")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(user_name,email,password)