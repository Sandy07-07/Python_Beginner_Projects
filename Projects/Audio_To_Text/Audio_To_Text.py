import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Load Audio File
audio_file = sr.AudioFile("Audio_To_Text.wav")

# Open the audio file using the recognizer
with audio_file as source:
    audio = r.record(source)

# Recognize the audio using Google Speech Recognition
text = r.recognize_google(audio)

# Print the recognized text from the audio
print(text)
