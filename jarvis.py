import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def atentions() :
    speak("I am jarvis! code verision 0.0.1, enginering you sir! Black Mamba")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<11:
        speak("Good Morning sir!")

    elif hour>=11 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    atentions()

def takeCommand():

    r = sr.Recognizer()
    mic = sr.Microphone()
    r.pause_treshold = 1

    while True :
        with mic as source:
            print("Listening...")
            audio = r.listen(source)
            print("Listening time out")
            
            try :
                query = r.recognize_google(audio, language = 'id-ID')
                print(f"User said: {query}\n")
            except sr.UnknownValueError:
                print("please try agian")
                return "none"
            except Exception as e:
                # print(e)
                print("Say the again please...")
                return "none"
            return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #controller AI

        if 'wikipedia' in query:
            speak("serching wikipedia...")
            query = query.replace("wikipedia", "")
            if not query :
                speak("sorry sir, i don't now")
            else :
                print(query)
                speak("in query wikipedia")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                
        elif 'halo jarvis' in query:
            speak("hello sir, can i help you")

        elif 'jarvis' in query:
            speak("yes sir")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("starting browsure url youtube.com")

        elif 'cari di youtube' in query:
            query = query.replace("cari di youtube","")
            if not query :
                speak("sorry sir, i don't now")
            else :
                webbrowser.open("https://www.youtube.com/results?search_query="+query)
                speak("find "+query+" in youtube.com")
