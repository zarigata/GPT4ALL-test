import ollama # Ollama
from ollama import Client
 


# --------------------------------------------- #


client = Client(host='http://localhost:11434')
response = client.chat(model='mistral:latest', messages=[{'role': 'user', 'content': {'text': 'hello'}, 'options' : {'num_ctx': 1024},}])

print(response['message']['content'])



# -------------------------------------------- #