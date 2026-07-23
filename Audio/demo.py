import sounddevice as sd
from scipy.io.wavfile import write, read
import tkinter as tk


root = tk.Tk()
 

SAMPLE_RATE = 44100
DURATION = 5  # seconds



def record():
    print("🎙  Recording for 5 seconds... Speak now!")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    write("output.wav", SAMPLE_RATE, audio)
    print("✅ Done recording!")
    
btn2 = tk.Button(root,text="Record!",command=record)
btn2.pack()

def play():
    print("🔊 Playing back...")
    rate, data = read("output.wav")
    sd.play(data, rate)
    sd.wait()
    print("✅ Done!")

btn1 = tk.Button(root,text="Play:)",command=play)
btn1.pack()

    

root.mainloop()

 

