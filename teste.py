
import ollama # Ollama
from ollama import Client
import time #i have no idea
import pyttsx3 #==============================================#
import speech_recognition as sr #import speech recognition module from Google.
import requests

#=============================#
def talk(text):
    engine.say(text)
    engine.runAndWait()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

recognizer = sr.Recognizer()

# Use default microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    print("Processing...")
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))\

def generate_text_with_prompt(prompt_text):
    url = 'http://valleteck.ddns.net:11434/api/generate'
    payload = {
        "model": "hub/donald-trump",
        "prompt": text,
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

fala = generate_text_with_prompt(text)
print ("Falando...", fala)
talk(fala)
        

    
