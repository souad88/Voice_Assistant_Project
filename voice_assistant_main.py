
# NOTE: this example requires PyAudio because it uses the Microphone class
#Work Well
import os
import playsound
from playsound import playsound
from gtts import gTTS
import time
from threading import Thread
import speech_recognition as sr
import concurrent.futures
#import open_google as g
import whatsapp_ as w
from pygame import mixer
import music_list_ as music 
import getweather as gw
import V4_last_work as tr
#trans=my_translate()
r = sr.Recognizer()
m = sr.Microphone()
#thread_
pool=concurrent.futures.ThreadPoolExecutor(max_workers=2)
def Device_Speak(audios):
    D = gTTS(text=audios, lang='en', slow=False)
    audioF = '/home/souad/Desktop/python_project/audio.mp3'
    D.save(audioF)
    playsound(audioF)
    print(audios)
    os.remove(audioF)
##chating    
def  voice_command(text): #talk and speak
          
    if text=='open WhatsApp': #Start thread
        print(text)
        tr.whatsapp_()
        #w.Whatsapp_open()
    if text=='play music':
        print(text)
        music.play_background() 
    if text=='weather':
       print(text) 
       tr.weather_()
       #current_temperature,weather_description,current_pressure=gw.current_weather('cairo')
       #Device_Speak("Current Temp
       # erature in cairo city is  ")
       #Device_Speak(current_temperature)
       #Device_Speak("Celsius")
       #Device_Speak("Current Pressure"+current_pressure)
       #Device_Speak("Weather description is "+weather_description)
    if text=='Translate': 
        tr.trans_()    
    if text=='close':
        print("closing.....")
        Device_Speak("good bye")
        exit(1)
        

#Recognizer function:
#recognizer=1        
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
       
        text=recognizer.recognize_google(audio)
       # print(recognizer.recognize_google(audio))
    
        voice_command(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
   

def Me_speak():

    with m as source:
        r.adjust_for_ambient_noise(source) 

 
    stop_listening = r.listen_in_background(m, callback)
    for _ in range(50): time.sleep(0.1)  
  
    while True: time.sleep(0.1)  # 
    while(1):
        stop_listening(wait_for_stop=False)
        time.sleep(5) 

    
########
if __name__=="__main__":
    Device_Speak("welcome in your voice assistant system")
    #Me_speak()
    pool.submit(Me_speak)
    pool.submit(voice_command)
    pool.shutdown(wait=True)
    
    