import enchant
import re
from deep_translator import GoogleTranslator
import requests

# Take input from terminal
print("Welcome to Language Translator!")
print("We will help you translate English to Spanish and French Audio Files.\n")

# carry out validation to check words inputed are english
# will only accept English words, can not accept names for example
d = enchant.Dict("en_US")
pattern = r"\W+" # match any non word character
repeat = True

while (repeat == True):
  text = input("Input english sentence to translate:")
  words = re.split(pattern, text)
  valid = True
  for w in words:
    if (w != ""):
      valid = d.check(w)
    if valid == False:
      repeat = True
  if (valid == True):
    repeat = False
  else:
    print("You inputted an invalid word, so can not translate!")
    print("Try again.\n")

# translate text to spanish using google language library
text_es = GoogleTranslator(source='auto',target='es').translate(text)
print(text_es)

# translate text to french using google language library
text_fr = GoogleTranslator(source='auto',target='fr').translate(text)
print(text_fr)

# convert translations to audio file and store
def getAudios(textToConvert, fileName):
  CHUNK_SIZE = 1024
  url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

  headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "36bd49e349f2ff5d0f702d5d10bf314c"
  }

  data = {
    "text": textToConvert,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
      "stability": 0.5,
      "similarity_boost": 0.5
    }
  }

  response = requests.post(url, json=data, headers=headers)
  with open(f'{fileName}.mp3', 'wb') as f:
      for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
          if chunk:
              f.write(chunk)

getAudios(text_es, "text_es")
getAudios(text_fr, "text_fr")