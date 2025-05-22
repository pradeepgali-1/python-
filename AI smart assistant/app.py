import google.generativeai as genai
from apikey import api_data
import os
import speech_recognition as sr
import pyttsx3
import webbrowser
genai.configure(api_key=api_data)
Model = "gemini-1.5-flash"
model = genai.GenerativeModel(model_name=Model)
def Reply(question):
    response = model.generate_content(
        f"You are a helpful assistant. {question}"
    )
    return response.text
#question = "In simple terms explain me AI not more than 50 words?"
#ans = Reply(question)
#print(ans)

#Text to Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak (text):
   engine.say(text)
   engine.runAndWait()
speak("Hello How are you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
       #wait for 1 sec before considering the end of a phrase
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio,language ='en-in')
        print("User said:{}\n".format(query))
    except Exception as e:
        print("say that again......")
        return "None"
    return query
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if query == "None":
            continue
        ans = Reply(query)
        print(ans)
        speak(ans)
        if "Open youtube" in query:
            webbrowser.open("www.youtube.com")
        if "Open youtube" in query:
            webbrowser.open("www.youtube.com")
        if "bye" in query:
            break