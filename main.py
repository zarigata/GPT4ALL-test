#defenition of classes and imports
import ollama
from ollama import Client
import speech_recognition as sr
import pyttsx3

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


client = Client(host='http://192.168.15.115:11434')
response = client.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': command,
  },
])
print(response['message']['content'])