import speech_recognition as sr
import datetime
import pywhatkit as wk
import speedtest
import os, datetime,time
from tkinter import *
import pyttsx3  
import os 
import pyautogui 
import requests 
from bs4 import BeautifulSoup
import wikipedia, webbrowser



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand(): 
  
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening...") 
        r.pause_threshold = 1 
        audio = r.listen(source) 
  
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 
  
    except Exception as e:     
        print("Say that again please...")   
        return "None" 
    return query 

 #Greet Me Function 

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        
#CONVERSATION--------------------------------------------------------
        
        if "buddy" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                 
                if "hello" in query:
                    speak("Hello sir,how are you ?")
                                  
                elif "i am fine" in query:
                    speak("well that's great, sir")
                
                elif 'what is your name' in query:
                    speak('My name is Jarvis and i am AI generated virtual voice assistance chatbot')
                    
                elif "how are you" in query:
                    speak("Perfect,sir")
                    
                elif "thank you" in query:
                    speak("you are welcome,sir")
                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                 
                elif "okay bye buddy" in query:
                    speak("Going to sleep,sir")
                    exit()
                
                elif "go to sleep" in query:
                    speak("Ok sir, I m going to take a nap, You can call me anytime")
                    break
                
                                    ############ Apps Automation #################

                elif "scroll down" in query: 
                    pyautogui.scroll(1000) 
                
                 
                elif "refresh" in query: 
                    pyautogui.moveTo(1551,551, 2) 
                    pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right') 
                    pyautogui.moveTo(1620,667, 1) 
                    pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left') 
                
                elif "drag visual studio to the right" in query: 
                    pyautogui.moveTo(46, 31, 2) 
                    pyautogui.dragRel(1857, 31, 2)
                       
                
                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                             
                
                    
# Wikipedia---------------------------------------------

                elif 'wikipedia' in query: 
                    speak('Searching Wikipedia...') 
                    query = query.replace("wikipedia", "") 
                    results = wikipedia.summary(query, sentences=2) 
                    speak("According to Wikipedia") 
                    print(results) 
                    speak(results) 
                
                elif 'ok jarvis' in query: 
                    speak("what should I search ?") 
                    qry = takeCommand().lower() 
                    webbrowser.open(f"{qry}") 
                    results = wikipedia.summary(qry, sentences=2) 
                    speak(results)
                    
# paint

                    
                elif "rectangular spiral" in query: 
                    pyautogui.hotkey('win') 
                    time.sleep(1) 
                    pyautogui.write('paint') 
                    time.sleep(1) 
                    pyautogui.press('enter') 
                    pyautogui.moveTo(100, 193, 1) 
                    pyautogui.rightClick 
                    pyautogui.click() 
                    distance = 300 
                    while distance > 0: 
                        pyautogui.dragRel(distance, 0, 0.1, button="left") 
                        distance = distance - 10 
                        pyautogui.dragRel(0, distance, 0.1, button="left") 
                        pyautogui.dragRel(-distance, 0, 0.1, button="left") 
                        distance = distance - 10 
                        pyautogui.dragRel(0, -distance, 0.1, button="left") 
                        
                        
                    
# youtube Controls -------------------------

                elif 'youtube' in query: 
                    speak("what you will like to watch ?") 
                    qrry = takeCommand().lower() 
                    wk.playonyt(f"{qrry}")
                
                elif 'just open youtube' in query:
                    webbrowser.open('youtube.com')
                
                elif 'search on youtube' in query: 
                    query = query.replace("search on youtube", "") 
                    webbrowser.open(f"www.youtube.com/results?search_query={query}") 
                    
                elif 'play' in query:
                    song= query.replace('play', '')
                    speak(f'playing ' + "sir")
                    wk.playonyt(song)
                
    
                elif "mute" in query: 
                    pyautogui.press("volumemute")
                    
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                
                elif "resume" in query:
                    pyautogui.press("k")
                    speak("video played")
                
              #  elif "mute" in query:
                  #  pyautogui.press("m")
                  #  speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
    
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                    
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    
                    
#TEMPERATURE AND WEATHER------------------------------------------------------------------------------------------
                 
                elif "temperature" in query:
                    search = " what is the current temperature in pune"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                     
                elif "weather" in query:
                    search = "how is the current weather in pune"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                    
#INTERNET SPEED----------------------------------------------------------------------------------------------------
                    
                elif "internet speed" in query:
                    speak("please wait for a while")
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                
               
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                    
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break


                #elif "ip address" in query: 
                 #   speak("Checking") 
                #try: 
                #   ipAdd = requests.get('https://api.ipify.org').text 
                #   print(ipAdd) 
                #   speak("your ip adress is") 
                 #  speak(ipAdd) 
                #except Exception as e: 
                #  speak("network is weak, please try again some time later") 
                
                
                

                       
                     
            
                
              
              

                    
                
              