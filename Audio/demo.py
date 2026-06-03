import sounddevice as sd
from scipy.io.wavfile import write, read

SAMPLE_RATE = 44100
DURATION = 5  # seconds

print("🎙  Recording for 5 seconds... Speak now!")
audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
sd.wait()
print("✅ Done recording!")

write("output.wav", SAMPLE_RATE, audio)

print("🔊 Playing back...")
rate, data = read("output.wav")
sd.play(data, rate)
sd.wait()
print("✅ Done!")
