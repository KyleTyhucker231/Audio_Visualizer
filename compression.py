from scipy.io import wavfile


filename = "guitar_loop.wav"
data = wavfile.read(filename)

data_array = data[1]    #extract the data array from the spot 2 of the tuple
                        #wavfile reads data from wav file as (samplerate, raw amp data)

print(*data_array)  






#i=0
#for element in data_array:
#    peak = data_array[i]
#    if peak < data_array[i+1]:
 #       peak = data_array[i+1]
#print(peak)


#print(*data_array)                  # prints all the elements of array
