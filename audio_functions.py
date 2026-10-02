from scipy.io import wavfile

#okay so the plan in the future is to have this file contain some very basic audio function
#that i can call in other file to keep the code nice and clean

filename = "guitar_loop.wav"
data = wavfile.read(filename)

# should normalize array to b -1 to 1 for data processing 
sample_rate = data[0]
samples = data[1]    


def adjust_volume(samples_array, volume_adjust):
        samples_array * volume_adjust
        return samples_array

def reverse_audio(samples_array):

        return samples_array

def splice_audio(start_index, end_index):

        return samples_array

print(samples)
print(adjust_volume(samples, 0.5))