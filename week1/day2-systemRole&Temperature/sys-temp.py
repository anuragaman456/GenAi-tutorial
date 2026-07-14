import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv();

myapi_key=os.getenv("GROQ_API_KEY")

client=Groq(api_key=myapi_key)

model="qwen/qwen3-32b"

role="user"
prompt="i love you baby"

message_system={
    "role":"system",
    "content": "she is you lover"
}

message={
    "role":role,
    "content":prompt
}

messages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messages,temperature=2)

ans=response.choices[0].message.content

print(ans)




