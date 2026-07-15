import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
# from 

load_dotenv()

myapi_key=os.getenv("GROQ_API_KEY")

client=Groq(api_key=myapi_key)

model="llama-3.1-8b-instant"
prompt1="hello"
prompt2="explain advantages and disadvantages for Ai in 100 words "
prompt3="explain advantages and disadvantages for Ai in 10 words"
prompt=[prompt1,prompt2,prompt3]
for prompts in prompt:
    message={
        "role":"user",
        "content":prompts
    }
    messages=[message]

    response=client.chat.completions.create(model=model,messages=messages,max_tokens=500)
    print (f"Message: {response.choices[0].message.content}")
    print("\n")
    print (f"Token uses by prompt;{response.usage.prompt_tokens}, Response_token:{response.usage.completion_tokens} and Total token:{response.usage.total_tokens}")
    print(f"finish reason:{response.choices[0].finish_reason}")
    print("############################")


