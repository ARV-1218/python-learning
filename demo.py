import requests
from playsound import playsound

word = input("Enter a word:")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

Re = requests.get(url,timeout=1)
val = Re.json()
