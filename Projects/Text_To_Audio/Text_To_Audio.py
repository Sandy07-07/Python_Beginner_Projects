from gtts import gTTS
from playsound import playsound
import os

# To take the text as input
my_text = input("Enter your text :- ")

# To select the language as English
language = "en"

# Converting the Text to Audio
my_obj = gTTS(text=my_text, lang=language, slow=False)

# To save the resulting audio file
my_obj.save("result.mp3")

print("Converting your Text to Audio")
print("Playing the Audio")

# To play the audio file
playsound("result.mp3")
print("Audio Playing Done")
