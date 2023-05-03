import pyaudio
import wave

# Creating a pyaudio object
audio = pyaudio.PyAudio()

# Open the audio stream for recording
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# record audio frames and store them in a list
frames = []

# To store audio frames in the list and stop when there us a Keyboard interrupt
try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass

# Stop the recording and close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio into a wav file
sound_file = wave.open("Voice_Recorder.wav", "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()
