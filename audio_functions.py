from scipy.io import wavfile


filename = "guitar_loop.wav"
data = wavfile.read(filename)

# should normalize array to b -1 to 1 for data processing 
sample_rate = data[0]
samples = data[1]    

def adjust_volume(samples_array, volume_adjust):
        samples_array * volume_adjust
        return samples_array

print(*samples)
print(adjust_volume(*samples, 0.5))