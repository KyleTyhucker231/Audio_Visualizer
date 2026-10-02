import wave
import pygame
import numpy
import pyaudio
import time

#okay somehow need to get my audio data processed for the function in the other files 
#import the functions, process the data, convert that alter sample data into a stream of bytes
#so pyaudio can read that into a stream and play that audio back
#first step 

filename = "guitar_loop.wav"
chunk = 1024                    # 1024 bits
w =  wave.open(filename, 'rb')  #rb means read binary, reads the file as binary
p = pyaudio.PyAudio()           #instaialize the pyaudio object


#open a new audio stream with the given parameters found from the guitar_wave.wav file
#find the sample width, channels, framerate etc using wave to find that info
stream = p.open(format=p.get_format_from_width(w.getsampwidth()), #sample width is the same as bit depth!!
                channels=w.getnchannels(),
                rate=w.getframerate(),
                output=True)


data  = w.readframes(chunk)

while data != b'':
    stream.write(data)
    data = w.readframes(chunk)


#close the audio stream and end the pyaudio object
stream.close()
p.terminate()


