
# Neuro Construct
# Includes functions for pre-build processing
# and construction of .WAV files for NeuroSynth

import math
import wave #reading and writing .wav files
import numpy as np
import matplotlib.pyplot as plt
import NeuroLib as NL
import NeuroNoise as NZ
import NeuroNote as NN
import NeuroWave as NW
import NeuroDyne as ND

# calculate the number of samples
def nsamples(sec):
    return(int(round(sec * 44100,0)))


def make_wave_positive(wave):
    """ make all harmonic overtones equal
    """

    # calculate integers to address where phases of the model switch
    a = min(wave)
    if a < 0:
        a = -a
    else:
        print("Wave is already positive.")
        return

    wave = wave + a

    return(wave)

def merge_stereo_chunk(left_wave, right_wave):
    """ merge a wave into a 2 channel stereo RIFF data chunk
    """
    chunk = list()

    left_time = len(left_wave)
    right_time = len(right_wave)
    if left_time != right_time:
        print("Failed to merge stereo data. Channels provided are not of equal length.")
        return

    for i in range(0,left_time,1):
        chunk.append(left_wave[i])
        chunk.append(right_wave[i])

    chunk = np.array(chunk, dtype = int)

    return(chunk)
def make_sample(x):
    sample = list()
    for i in range(0,len(x),1):
        sample.append(int(round(x[i],0)))
    return(sample)
