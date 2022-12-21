import datetime
import os
import time
import webbrowser  # to open web browser

import pyttsx3 as p
import speech_recognition as sr  # to recognize sound

from selenium_web import infow
from news import news

# to choose male or female :
engine = p.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 180)
voices = engine.getProperty("voices")
n = int(input("Write 0 For Male or 1 for female: "))
engine.setProperty("voice", voices[n].id)
r = sr.Recognizer()
mic = sr.Microphone(4)


def speak(text):
    engine.say(text)
    engine.runAndWait()


# to input record
def record_audio(ask=''):  # input your sound and record it
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening........")
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en-us")  # to run sounds
        except sr.UnknownValueError:  # if found  error (لو دخلت كلام غير مفهوم (
            speak("Sorry, I don't understand you,sir")
        except sr.RequestError:  # if found error in request (like internet)
            speak('sorry my service is down right now')
        return voice_data.lower()


def wishMe(name):
    hour = int(datetime.datetime.now().hour)  # get The Time Now
    if 0 <= hour < 12:
        speak(F"Good Morning {name} !")
    elif 12 <= hour < 18:
        speak(F"Good Afternoon {name} !")
    else:
        speak(F"Good Evening {name} !")


def respond(voice_data):
    if "what's your name" in voice_data:
        speak('My name is husso,tell me your name :')

    elif "what's the time" in voice_data:
        speak(time.ctime())

    elif "youtube" in voice_data:
        print("Youtube")
        s = record_audio('what do you want Me to search for : ')
        url = 'https://www.youtube.com/results?search_query='+s
        webbrowser.get().open(url)
        speak('here is what I found for U : '+s)

    elif 'search' in voice_data:
        search = record_audio('what do you want Me to search for : ')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('here is what I found for U : ' + search)
    elif "news" in voice_data:
        for i_news in news():
            speak(i_news)

    elif 'find the location' in voice_data:
        location = record_audio('whast is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('here is the location you want : ' + location)

    elif "information" in voice_data:
        info_to_search = record_audio("you need information related to which topic ? ")
        speak(infow().get_info(info_to_search))

    elif 'open download' in voice_data:
        os.startfile(r'C:\Users\NourEldin\Downloads')

    elif 'close' in voice_data:
        speak('bye ')
        exit()


name = record_audio("What's your name")
wishMe(name)
speak("Hello world, My name is husso , I,m your voice assistant")
speak('How can I help you?')
while 1:
    r_voice_data = record_audio()
    print(r_voice_data)
    respond(r_voice_data)
