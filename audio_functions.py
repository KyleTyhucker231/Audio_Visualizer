from scipy.io import wavfile
import numpy as np

#okay so the plan in the future is to have this file contain some very basic audio function
#that i can call in other file to keep the code nice and clean

filename = "guitar_loop.wav"
data = wavfile.read(filename)

# should normalize array to b -1 to 1 for data processing 
sample_rate = data[0]
samples = data[1]    

#adjusts the volume of audio based on given metric
def adjust_volume(samples_array, volume_adjust):
        samples_array * volume_adjust
        return samples_array

#reverses the sample array to invert audio
def reverse_audio(samples_array):
        reversed_array = samples_array[::-1]
        return samples_array

#splices section of samples based on given start and end index
def splice_audio(samples_array, start_index, end_index):
        spliced_array = samples_array[start_index:end_index]
        return spliced_array

#converts given samples array to bytes
def audio_to_bytes(samples_array):
        bytes_array = samples_array.tobytes()
        return bytes_array


print(samples.dtype)
#print(samples)
#print(adjust_volume(samples, 0.5))