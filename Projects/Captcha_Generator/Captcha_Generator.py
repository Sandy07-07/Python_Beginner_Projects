from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
from playsound import playsound

var = input("Enter character to create Captcha from :- ")
img = ImageCaptcha()  # The ImageCaptcha class is instantiated
data = img.generate_image(var)  # It generates the captcha image with given text
img.write(var, '1.png')  # It writes the generated captcha image in the given format in the same directory

aud = AudioCaptcha()   # The AudioCaptcha class is instantiated
data1 = aud.generate(var)  # It generates the captcha audio with given text
aud.write(var, '1.wav')  # It writes the generated captcha audio in the given format in the same directory
playsound("1.wav")  # Plays the generated the audio captcha
