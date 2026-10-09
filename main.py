import numpy
import pyaudio
from scipy.io import wavfile
import audio_functions

#read the wavfile, transfer data into a samples array
filename = "guitar_loop.wav"
data = wavfile.read(filename)
sample_rate = data[0]
samples = data[1]    

chunk = 1024                    # 1024 bits

p = pyaudio.PyAudio()           #instaialize the pyaudio object


#open a new audio stream with the given parameters found from the guitar_wave.wav file
#find the sample width, channels, framerate etc using wave to find that info
stream = p.open(format=pyaudio.paInt16,
                channels=2, 
                rate=sample_rate,
                output=True)

for i in range(0, len(samples), chunk):
    current_chunk = samples[i:i+chunk]
    stream.write(current_chunk.tobytes())


#close the audio stream and end the pyaudio object
stream.close()
p.terminate()


