#Auther :Souad Gamal#
#jack_control start
from ctypes import *
import speech_recognition as sr
import pyttsx3 as py #install pyttsx3 ,libespeak1 
import playsound 
import pyaudio
from gtts import gTTS
import os
import time
from translate_ import my_translate
#import music_list_ as music 
import translate_ as trr
import getweather as gw
import whatsapp_ as w

trans=my_translate()

def speak(audios):
    tts = gTTS(text=audios, lang='en', slow=False)
    audioF = 'audio.mp3'
    tts.save(audioF)
    playsound.playsound(audioF)
    print(audios)
    os.remove(audioF)

r=sr.Recognizer()
def Me_talk():
    with sr.Microphone() as source:
        
        #r.energy_threshold=10000
        #r.adjust_for_ambient_noise(source,1.2)
        print("listening.........")
        my_voice=r.listen(source)
     
        try:
            text = r.recognize_google(my_voice)
            print(text)
            return text
        except:
            speak("what...Repeat again")
            Me_talk()
def trans_():            
    speak("what is the text")
    t_text=Me_talk() 
    speak("to which language?")
    dst_lang_text=Me_talk()
    if(dst_lang_text=='German'):
        dst_lang_text='de'
        time.sleep(3.0)
    if(dst_lang_text=='French'):
        dst_lang_text='fr'     
        time.sleep(3.0)
    trans_s=trans.translateText(t_text,dst_lang_text) #add more seconds if text is so long
    #trans_s=trr.translateText_ts(t_text,src_lang_text,dst_lang_text)
    #print("translated"+trans_s)
    speak(trans_s)
   
def check_contact_(): 
   speak("which contact ?")
   contact=Me_talk()
   t=w.check_contact(contact)
   return t,contact
def whatsapp_():
        speak("what is next ?")
        text=Me_talk()
        time.sleep(0.2)
        #send messags through whats app
        if(text=='message'):
            speak("what is the message")
            message=Me_talk()
            #check if contact in the contact list or not
            t,contact=check_contact_()
            time.sleep(0.1)
            if(t==True):
                w.Whatsapp_open(message,contact)
                time.sleep(0.1)
            else:
              speak("there is no contact with such name in your list")
                      
                    
def music_():
    pass        
 #music.play_background() 
        
def weather_():

       speak('which city ?')
       city=Me_talk() 
       current_temperature,weather_description,current_pressure=gw.current_weather(city)
       speak("Current Temperature in"+city+" city is: ")
       speak(current_temperature)
       speak("Celsius")
       speak("Current Pressure "+current_pressure)
       speak("Weather description is "+weather_description)  
        
#trans_()        
#weather_()
#whatsapp_()