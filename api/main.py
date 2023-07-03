from flask import Flask
import datetime
import os
import webbrowser as wb
import speech_recognition as sr
import wikipedia
import pyjokes
import pyttsx3
import pywhatkit

app = Flask(__name__)

@app.route('/')
def test():
    return 'Say hi to Jarvis motherfuckers'

@app.route('/api/talkback')
def talkback():
    print('talkback running')
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def talk(text):
        engine.say(text)
        engine.runAndWait()

    def take_command():
        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in')
            print(f"User said: {command}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"

        return command

    def run_jarvis():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            print(time)
            talk('Current time is:' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'open' in command:
            infor = command.replace('open', '')
            ans = wb.get(chrome_path).open(infor)
            talk('Opening The site..')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'who made you' in command:
            talk("I was built by Nirzar")
            print("I was built by Nirzar")
        elif 'ppt' in command:
            talk("opening Power Point presentation")
            loc = r"C:\Users\nirza\OneDrive - vit.ac.in\Desktop\My Mini Jarvo"
            os.startfile(loc)
        elif 'exit' in command:
            talk("Thanks for giving me your time")
            exit()
        else:
            talk('Please say the command again.')

    while True:
        run_jarvis()
    return 'chatbot working'


if __name__ == '__main__':
    print('main app running')
    app.run(debug=True)
