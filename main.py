from ollama import Client
client = Client(host='192.168.15.115:11434')
# Original request
response = client.chat(model='llama2-uncensored', messages=[
{
    'role': 'user',
    'content': input('Enter your message: ',), # Added a user input field
  },
])
print(response['message']['content'])
# make a new check