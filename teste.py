
import ollama # Ollama
from ollama import Client
import time #i have no idea
import pyttsx3 #==============================================#
import speech_recognition as sr #import speech recognition module from Google.

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

modelfile='''
FROM llama2
SYSTEM 
'''

ollama.list()
        
client = Client(host='http://192.168.15.115:11434')
response = client.chat(model='aladdin:latest', messages=[{'role': 'user','content': text,},])

print(response['message']['content'])
talk(response)
        

    