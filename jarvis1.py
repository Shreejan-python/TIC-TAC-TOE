import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import webbrowser
import random
import pyjokes



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good morning sir. I am virtual assistant JARVIS. How may I help you ?")
    elif hour >= 12 and hour<18:
        speak("Good afternoon sir. I am virtual assistant JARVIS. How may I help you ?")
    else:
        speak("Good night sir. I am virtual assistant JARVIS. How may I help you ?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        text = r.recognize_google(audio, language = 'en-in')
        print(text)

    except Exception:
        speak("Error..")
        print("Network Connection error...")
        return "none"
    return text

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query or 'who is' in query or 'where is' in query or 'what do you mean by' in query:
            speak("searching details....Wait!")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query or 'open video online' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("opening google")

        elif 'open word' in query or 'open microsoft word file' in query:
            wpath = '"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"'
            os.startfile(wpath)
            speak("Opening word")
        
        elif 'open PowerPoint' in query or 'open ppt' in query:
           fpath = '"C:\Program Files\Microsoft Office\\root\Office16\POWERPNT.EXE"'
           os.startfile(fpath)
           speak("Opening power point")


        elif 'open excel' in query or 'open microsoft excel file' in query:
            epath ='"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"'
            os.startfile(epath)
            speak("Opening excel")
        elif 'what is the time' in query:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time)
            speak("the time is " + time)
        elif 'good bye' in query:
            speak("good bye sir. Thank you for using me. And at last thank you to Shreejan sir who have build me.")
            exit()
        elif 'what\'s up' in query or 'how are you' in query:
            stMsgs = ['Just doing my thing', 'I am fine', 'I am nice and full of energy', 'I am fine. How are you ?']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_how_are_you = takecommand()
            if 'fine' in ans_how_are_you or 'good' in ans_how_are_you or 'okay' in ans_how_are_you:
                speak("Okay sir..")
            elif 'not fine' in ans_how_are_you or 'not good' in ans_how_are_you or 'sick' in ans_how_are_you:
                speak("extremely sorry sir..")
        elif 'make you' in query or 'programmed you' in query:
            ans_op = "For your kind information Sir Shreejan Dolai has made me using python programming language on visual studio code editor on dell inspiron 3501 laptop"
            speak(ans_op)
            print(ans_op)
        elif 'open git hub' in query or 'open git' in query:
            webbrowser.open("www.github.com")
            speak("Opemimg git hub")
        elif 'tell a joke' in query or 'please tell a joke' in query:
            joke_1 = pyjokes.get_joke()
            speak(joke_1)
        elif 'I want to do addition' in query or 'add this' in query:
            ans_add = "Yes sir please write the numbers here"
            speak(ans_add)
            num_add = int(input("Enter your first number :"))
            num_add2 = int(input("Enter your second number :"))
            ans_of_add = int(num_add) + int(num_add2)
            speak("Your answer is :")
            print(ans_of_add)
        elif 'I want to do subtraction' in query or 'subtract this' in query:
            ans_minus = "Yes sir please write the numbers here"
            speak(ans_minus)
            num_minus = int(input("Enter your first number :"))
            num_minus_2 = int(input("Enter your second number here :"))
            ans_of_minus = int(num_minus) - int(num_minus_2)
            speak("Your answer is :")
            print(ans_of_minus)
        elif 'multiply this' in query or 'I want to do multiplicaton' in query:
            ans_mu = "Yes sir please enter your number here" 
            speak(ans_mu)
            num_mu = int(input("Enter your first number :"))
            num_mu_2 = int(input("Enter your second number here :"))
            num_mu_ans = int(num_mu) * int(num_mu_2)
            speak("Your result is :")
            print(num_mu_ans)
        elif 'divide this' in query or 'I want to divide' in query:
            speak("Sir please enter the numbers here")
            num_pd = int(input("Enter your first number :"))
            num_pd2 = int(input("Enter your second number :"))
            speak("Your answer is given below. Please check this ")
            print(int(num_pd) / int(num_pd2))