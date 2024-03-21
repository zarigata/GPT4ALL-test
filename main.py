#defenition of classes and imports
import ollama
from ollama import Client
import speech_recognition as sr
import pyttsx3
import requests





listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'gladys' in command:
                command = command.replace('gladys', '')
                print(command)
    except:
        pass
    return command
#continue running
rodar = 1
command = take_command()


def generate_text_with_prompt(prompt_text):
    url = 'http://valleteck.ddns.net:11434/api/generate'
    payload = {
        "model": "aladdin:latest",
        "prompt": command,
        "stream": False,
        "options": {
            "num_ctx": 1024
        }
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        response_json = response.json()
        if "response" in response_json:
            return response_json["response"]
        else:
            print("Response does not contain 'response' key.")
            return None
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None

#print(response['message']['content'])