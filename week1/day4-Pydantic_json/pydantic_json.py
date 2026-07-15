import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
import json

load_dotenv()

myapi_key=os.getenv("GROQ_API_KEY")

client=Groq(api_key=myapi_key)

class Ticket(BaseModel):
    name:str
    email:str
    phone_number:int
    issue:str

schema=Ticket.model_json_schema()

response_format={
    "type":"json_object"
}

model="llama-3.1-8b-instant"
text="hi my name is anurag aman and my emial id is anurag.nitm@gmail.com and and my phone number is 8358856184 and currenlt my paymnet got failed which is oh $100"

# system_prompt=f"""
#     please extract all the personal information from this in json format
#     {text}
# """

system_prompt=f"""
    Extract the personal information from the ticket strictly based on this schema and give a json output 
    {schema}
"""
system_message={
    "role":"system",
    "content":system_prompt

}

message ={
    "role":"user",
    "content":text
}

messages=[system_message,message]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)

print(response.choices[0].message.content)

new_json=response.choices[0].message.content

final_ans=json.loads(new_json)

ticket=Ticket(**final_ans)

print(ticket.name)

