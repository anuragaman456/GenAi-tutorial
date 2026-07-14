import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv();

myapi_key=os.getenv("GROQ_API_KEY")

client=Groq(api_key=myapi_key)

model="llama-3.3-70b-versatile"

role="user"
prompt="i love you baby reply"

prompt2="suggest me some name for my electronic business"

# message_system={
#     "role":"system",
#     "content": "she is your lover"
# }

message_system={
    "role":"system",
    "content": "she is your boss"
}



# System Role tells the AI who it is and how it should behave throughout the conversation
# ex->"content": "she is your lover"
# ex->"content": "she is your boss"

message={
    "role":role,
    "content":prompt2
}

# messages=[message_system, message]

messages=[message] #-> for temperature

# Temperature controls how random or creative the AI's response is.
# Low temperature (0.0–0.3) → More predictable, consistent, factual.
# Medium (0.5–0.7) → Balanced.
# High (0.8–2) → More creative, varied, less predictable.
#temperature mostly lies between 0-2

response=client.chat.completions.create(model=model, messages=messages,temperature=0.1)

# ans=response.choices[0].message.content

# print(response)

print("#####################################")

print(response.choices[0].message.content)




