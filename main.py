import os
import speech_recognition as sr

command2mp3 = "ffmpeg -i Example.mp4 Example.mp3"
command2wav = "ffmpeg -i Example.mp4 Example.wav"

os.system(command2mp3)
os.system(command2wav)

r = sr.Recognizer()
with sr.AudioFile('Example.wav') as source:
    audio = r.record(source, duration=20)
    try:
        print("working on...")
        print(r.recognize_google(audio))
    except:
        print("Sorry run again...")

