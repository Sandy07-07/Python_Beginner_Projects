import moviepy.editor
from tkinter.filedialog import *
from playsound import playsound

# To select the file form the system
vid = askopenfilename()
video = moviepy.editor.VideoFileClip(vid)  # Pass the file as an argument to be used for various operations

aud = video.audio  # To extract the audio track from the video file
aud.write_audiofile("Video_To_Audio_Converted.mp3")  # To extract the audio file to the specified audio file format

print("File Conversion of Video to Audio Completed")
print("Playing the Converted Audio")
playsound("Video_To_Audio_Converted.mp3")  # To play the extracted audio file
