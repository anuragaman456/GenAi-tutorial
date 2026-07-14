import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv();

myapi_key=os.getenv("GROQ_API_KEY")

client=Groq(api_key=myapi_key)

model="llama-3.1-8b-instant"

role="user"
prompt="tell me about palindrome"

message={
    "role":role,
    "content":prompt
}

messages=[message]

response=client.chat.completions.create(model=model, messages=messages)

print(response);

print("-----------------------")

finalResponse=response.choices[0].message.content


print(finalResponse)

