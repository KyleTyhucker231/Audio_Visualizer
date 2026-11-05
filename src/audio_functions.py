import numpy as np

#adusts the volume of audio based on given metric
def adjust_volume(samples_array, volume_adjust):
        adjusted = samples_array.astype(np.float64) * volume_adjust
        return adjusted.astype(samples_array.dtype)

#reverses the sample array to invert audio
def reverse_audio(samples_array):
        reversed_array = samples_array[::-1]
        return reversed_array

#splices section of samples based on given start and end index
def splice_audio(samples_array, start_index, end_index):
        spliced_array = samples_array[start_index:end_index]
        return spliced_array
