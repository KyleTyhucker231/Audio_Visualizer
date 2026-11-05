from scipy.io import wavfile

#this file will contain all the functions for performing audio compression on the file
#it will return the audio with compression added

#so some variables or parameters ill likely need to add
#THRESHOLD, RATIO, ATTACK, RELEASE, MAKE-UP GAIN 
#no knee for now but maybe in later implementation
# create a definition for a compressor audio object

filename = "guitar_loop.wav"
data = wavfile.read(filename)

# should normalize array to b -1 to 1 for data processing 
sample_rate = data[0]
data_array = data[1]    #extract the data array from the spot 2 of the tuple
                        #wavfile reads data from wav file as (samplerate, raw amp data)



threshold: float =  -20.0         #in dBFS
ratio: float = 4.0               
attack_ms: float = 1.0
release_ms: float = 1.0
make_up_gain: float = 2.0

#return audio compressed
#output = input - ((threshold/ratio) + threshold)
def compression():

    return 


#print(*data_array)  






#i=0
#for element in data_array:
#    peak = data_array[i]
#    if peak < data_array[i+1]:
 #       peak = data_array[i+1]
#print(peak)


#print(*data_array)                  # prints all the elements of array
