import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import wikipedia
import datetime as dt
import googlesearch
import sys
import requests,json
os.system("color 02")
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)



def start_wish():
    c_hour=dt.datetime.now().hour
    if c_hour >=0 and c_hour < 12:
        speak("Good  Morning sir")
    elif c_hour >=12 and c_hour < 15:
        speak("Good  afternoon  sir")
    elif c_hour >=15 and c_hour < 23:
        speak("Good  evening  sir")
def time():
    t=dt.datetime.now().strftime('%H,%M')
    speak(t)
    print(t)
def speak(voice_comm):
    engine.say(voice_comm)
    engine.runAndWait()
def voice_recong():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        audio=r.listen(source)  
    try:
        print("Recognizing your voice please wait")
        query=r.recognize_google(audio,language="en-in")
        print("User : ",query)
    except Exception as e:
        query="Nothing"
        print(e)
        print("sir, sorry i can't hear you!!!.  Ensure that you connected with internet and  check your microphone  works properly")
    query=query.lower()
    return query
def shutdown():
    speak("sir,   your  'command' is shutdown.")
    speak("if you want to set timer for shutdown?")
    t_set=voice_recong()
    if 'yes' in t_set or "s" in t_set or "ama" in t_set:
        speak("How many seconds?")
        t=voice_recong()
        t=t.replace("seconds","")
        os.system("shutdown /s /f /t {}".format(t))
        sys.exit()
    elif "no" in t_set or "venna" in t_set:
        speak("sir, I'm going to shutdown this computer    bye. create me to accuss every device as soon as posible ")
        os.system("shutdown /s /f /t 3")
        sys.exit()
    else:
        speak ("say  that  again  sorry!")



if __name__=="__main__":
    start_wish()
    query=voice_recong()

    if "open youtube" in query:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "google" in query:
        
        speak("opening google   by your default browser.")
        webbrowser.open("http://www.google.com/")
    elif "firefox"in query:
        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        speak("sir, Opening Firefox web browser")
    elif "chrome" in query:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        speak("sir, Opening Chrome")
    elif "play music"  in query or "song" in query or "music" in query:
        
        try: 
            list_ofSongs =os.listdir("E:\Srini 320kbs")
            os.startfile(os.path.join("E:\Srini 320kbs",list_ofSongs[5]))
        except:
            speak("sir, please enter the path where songs are there")
            path=input("NICOLA : sir, please enter the path where songs are there")
            list_ofSongs =os.listdir(path)
            os.startfile(os.path.join(path,list_ofSongs[0]))
    elif "demonstrate yourself" in query:

        Nicola_info= '''I'M  Mister Nicola.   A.I. an artificial intelligence developed by  srinivasan.  He is
        not just my developer he is everything.  he is the person one who gave a birth.
        and i can do every thing for srini. I'm protected my him.  he developed 
        safest artificial intelligence that's me. The name Nicola.   inspired by sir Nicoal Tesla the great inventer '''
        speak(Nicola_info) 
    elif "time"in query:
        time()
    elif "wikipedia"in query  or "explain about" in query:
        query=query.replace("what is","")
        query=query.replace("explain about","")
        query=query.replace("wikipedia","")
        fullreport=wikipedia.summary(query)
        report=wikipedia.summary(query,sentences=2)
        print(fullreport)
        speak(report)
    elif "search" in query or "link" in query or "site" in query :
        query=query.replace("search","")
        query=query.replace("link","")
        query=query.replace("site","")
        site_url=googlesearch.search(query)
        webbrowser.open_new(site_url[0])
        speak("sir, first link ka open paannirrukan verra site  paaka laama?")
        q_site=voice_recong()
        for i in range(len(site_url)) :
            if "next" in q_site:
                webbrowser.open_new(site_url[i+1])
                q_site=voice_recong()
            else:
                break
    elif "shutdown" in query:
        shutdown()
    elif "restart" in query:
        speak("this computer will restart now.    Remember to activate me")
        os.system("shutdown /r")
    elif "log off" in query:
        speak("I'm going to logoff.    bye")
        os.system("shutdown /l /f")