import numpy
import pyaudio
from scipy.io import wavfile
from pathlib import Path
import audio_functions as af

#read the wavfile, transfer data into a samples array
filename = Path(__file__).parent / 'guitar_loop.wav'
data = wavfile.read(filename)
sample_rate = data[0]
samples = data[1]    

chunk = 1024                    # 1024 frames

p = pyaudio.PyAudio()           #intialize the pyaudio object


#open a new audio stream with the given parameters found from the guitar_wave.wav file
#find the sample width, channels, framerate etc using wave to find that info
stream = p.open(format=pyaudio.paInt16,
                channels=2, 
                rate=sample_rate,
                output=True)

#here lets try to alter the data before we read through it and play it back

#samples = af.reverse_audio(samples)
samples = af.adjust_volume(samples, 1.2)

for i in range(0, len(samples), chunk):
    current_chunk = samples[i:i+chunk]
    stream.write(current_chunk.tobytes())


#close the audio stream and end the pyaudio object
stream.close()
p.terminate()


