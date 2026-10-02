from scipy.io import wavfile

#so some variables or parameters ill likely need to add
#THRESHOLD, RATIO, ATTACK, RELEASE, MAKE-UP GAIN 
#no knee for now but maybe in later implementation
# create a definition for a compressor audio object

filename = "guitar_loop.wav"
data = wavfile.read(filename)

# should normalize array to b -1 to 1 for data processing 

data_array = data[1]    #extract the data array from the spot 2 of the tuple
                        #wavfile reads data from wav file as (samplerate, raw amp data)

threshold = -20         #in dBFS
ratio = 4               
attack_ms = 1
release_ms = 1
make_up_gain = 2

def compression():




#print(*data_array)  






#i=0
#for element in data_array:
#    peak = data_array[i]
#    if peak < data_array[i+1]:
 #       peak = data_array[i+1]
#print(peak)


#print(*data_array)                  # prints all the elements of array
