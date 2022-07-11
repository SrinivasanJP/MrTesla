import speech_recognition as sr
import pyttsx3
import datetime
import requests,json
import pandas as pd
import os
import random
import googlesearch
import webbrowser
import wikipedia
import sys
def voice_comm():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.adjust_for_ambient_noise(source)
        voice=r.listen(source,phrase_time_limit=5)
    try:
        print("Recognizing your voice please wait...")
        query=r.recognize_google(voice)
        print("User said :",query)
    except Exception :
        print('''sorry i can't recognize you voice.
         please make sure you connected with internet and 
         your microphone works properly''')
        query=""
    return query.lower()
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("rate",178)
engine.setProperty('voice',voices[1].id)

def speak(comm):
    engine.say(comm)
    engine.runAndWait()
def time():
    t=datetime.datetime.now()
    print(t.strftime("%I:%M   %p"))
    speak(t.strftime("%I:%M   %p"))
def c_date():
    d=datetime.date.today()
    print(d.strftime("%d-%B-%Y"))
    speak(d)
def wish_me():
    c_hour=datetime.datetime.now().hour
    if c_hour >=0 and c_hour < 12:
        speak("Good  Morning sir")
    elif c_hour >=12 and c_hour < 15:
        speak("Good  afternoon  sir")
    elif c_hour >=15 and c_hour < 24:
        speak("Good  evening  sir")
    
def set_cityname_and_Country(voice_city):
    voice_city=voice_city.split()
    col_name=["city","country"]
    df=pd.read_csv('worldcities.csv',usecols=col_name)
    city_name=""
    country_name=""
    cities=list(df["city"])
    cities=[x.lower() for x in cities]
    country= list(df["country"])
    country=[x.lower() for x in country]
    for i in range(len(voice_city)):
        for j in range (len(cities)):
            if voice_city[i]==cities[j]:
                city_name=voice_city[i]
                return city_name
                
    for i in range(len(voice_city)):
        for j in range (len(country)):
            if voice_city[i]==country[j]:
                country_name=voice_city[i]
                return country_name
def weather(voice_w):
    city=set_cityname_and_Country(voice_w)
    city_name=""
    if city==None:
         city_name="alinjikuppam"
    else:
        city_name=city
    '''this is the url to access the api site'''
    complete_url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + "c0c231d75a666eed4b1caec29d778120" + "&q=" + city_name
    '''request sent to url and recieve as json format '''
    data_injson = requests.get(complete_url)
    #converting json to python
    data_inPY = data_injson.json()
    #if the city not found it display as 404 error
    if data_inPY["cod"] != "404":
    
        # store the value of "main"
        # key in variable y
        y = data_inPY["main"]
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
    
        # store the value correspondingche
        # to the "humidity" key of y
        current_humidity = y["humidity"]
    
        # store the value of "weather"
        # key in variable z
        z = data_inPY["weather"]
    
        # store the value corresponding
        # to the "description" key at
        # the 0th indedata_inPY of z
        weather_description = z[0]["description"]

        if "temperature" in voice_w:
            print("The Temperature is "+"%.2f"%(current_temperature-273.15)+" degree Celsius")
            speak("The Temperature is  "+"%.2f"%(current_temperature-273.15)+"   degree Celsius")
        elif "sky" in voice_w or "clouds" in voice_w:
            print("sky looks little "+str(weather_description)) 
            speak("sky looks little "+str(weather_description))
        elif "pressure" in voice_w:
            print("Pressure is "+str(current_pressure)+ " Pa")
            speak("Pressure is "+str(current_pressure)+ " Pa")
        elif "humidity" in voice_w:
            print("Humidity  is "+str(current_humidity)+" %")
            speak("Humidity  is "+str(current_humidity)+" %")
        else:
            print("The Temperature is "+"%.2f"%(current_temperature-273.15)+" degree Celsius")
            speak("The Temperature is  "+"%.2f"%(current_temperature-273.15)+"   degree Celsius")
            print("sky looks little "+str(weather_description)) 
            speak("sky looks little "+str(weather_description))
            print("Humidity  is "+str(current_humidity)+" %")
            speak("Humidity  is "+str(current_humidity)+" %")
            print("Pressure is "+str(current_pressure)+ " Pa")
            speak("Pressure is "+str(current_pressure)+ " Pa")
def Music():
    add=[]
    rar=[[root,files] for (root,dir,files) in os.walk("..",topdown=True) if files]
    for i in range(len(rar)):
        for j in range(len(rar[i])):
            #accessing main list which as [root,[files]]
            for k in range(len(rar[i][j])):
                #accessing sub list which as [files]
                for l in range(len(rar[i][j][k])):
                    #accessing each elements of sub_list that is files
                    if ".mp3" in rar[i][j][k]:
                        #print(rar[i][j][k])
                        #print(rar[i][0])
                        add.append(os.path.join(rar[i][0],rar[i][j][k]))
    
    os.startfile(random.choice(add))
def search_files(file_n,loc=".."):
    address=[]
    ra_file=[[root,files] for (root,dir,files) in os.walk("{}".format(loc),topdown=True) if files]
    for i in range(len(ra_file)):
        for j in range(len(ra_file[i])):
            #accessing main list which as [root,[files]]
            for k in range(len(ra_file[i][j])):
                #accessing sub list which as [files]
                for l in range(len(ra_file[i][j][k])):
                    #accessing each elements of sub_list that is files
                    if "{}".format(file_n) in ra_file[i][j][k]:
                        #print(ra_file[i][j][k])
                        #print(ra_file[i][0])
                        address.append(os.path.join(ra_file[i][0],ra_file[i][j][k]))
    return address
def site_links(q):
    return googlesearch.search(q)
def opening_google(q):
    webbrowser.open("https://www.google.com/")

def site_search(q):
    webbrowser.open_new_tab(site_links("{}".format(q))[0])



if __name__=="__main__":
    wish_me()
    query=voice_comm()
    
    if "weather" in query or "temperature" in query or "sky" in query or "clouds" in query or "pressure" in query or "humidity" in query :
        query=query.replace("weather","")
        weather(query)
    if "music" in query or "songs" in query:
        speak("Sir, I Gonna enjoy with you!")
        Music()
        while True:
            nextQ=voice_comm()
            if "next" in nextQ:
                speak("Okey")
                Music()
            else:
                break
    if "time" in query:
        time()
    if "date" in query :
        c_date()
    if "explain about" in query or "wikipedia" in query or "what is" in query:
        query.replace("explain about","")
        query.replace("wikipedia","")
        query.replace("what is","")
        print("Accourding to wikipedia.")
        print(wikipedia.summary(query))
        speak("Accourding to wikipedia.")
        speak(wikipedia.summary(query,sentences=5))
    if "search" in query or "link" in query or "site" in query or "page" or "who is" in query :
        query=query.replace("search","")
        query=query.replace("link","")
        query=query.replace("site","")
        query=query.replace("page","")
        query=query.replace("who is","")
        
        site_url=list(googlesearch.search(query))
        print(site_url)
        webbrowser.open_new(site_url[0])
        speak("sir, first link ka open paannirrukan verra site  paaka laama?")
        q_site=voice_comm()
        for i in range(len(site_url)) :
            if "next" in q_site:
                webbrowser.open(site_url[i+1])
                q_site=voice_comm()
            else:
                break        
    if "demonstrate yourself" in query:

        Tesla= '''I'M  Mister Tesla.   A.I. an artificial intelligence developed by  Srinivasan J P. 
         He is not just my developer he is everything.  he is the person one who gave a birth.
        and i can do every thing for srini. I'm protected my him.  he developed 
        safest artificial intelligence that's me. The name Nicola.   inspired by sir Nicoal Tesla the great inventer '''
        print(Tesla)
        speak(Tesla)     
    if "shutdown" in query:
        speak("Sir, I'm going to Shutdown this Computer    Bye. Create me   to Accuss every device as soon as Posible ")
        os.system("shutdown /s /f /t 3")
        sys.exit()
    if "restart" in query:
        speak("This computer will restart now.    Remember to Activate me")
        os.system("shutdown /r")
    if "log off" in query:
        speak("I'm going to Logoff.  Bye")
        os.system("shutdown /l /f")
    if "firefox"in query:
        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        speak("Sir, Opening Firefox web browser")
    if "chrome" in query:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        speak("Sir, Opening Chrome")
    if "open youtube" in query:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")

    