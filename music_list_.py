import multiprocessing 
import time 
from pygame import mixer
def play_music():
    mixer.init()
    mixer.music.load("/home/souad/Desktop/python_project/google_speech_2/YourMusicLocation.mp3")
    mixer.music.play()
    while mixer.music.get_busy():  
        time.sleep(1)
def foo():
    name = multiprocessing.current_process().name
    

def play_background():
        background_process = multiprocessing.Process(name=play_music(),target=foo) 
        background_process.daemon = True 
        