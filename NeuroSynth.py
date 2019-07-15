
import wave #reading and writing .wav files
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import gamma
import scipy.io.wavfile as spw
#import NeuroLib as NL
import NeuroConstruct as NC
import NeuroNoise as NZ
import NeuroNote as NN
import NeuroWave as NW
import NeuroDyne as ND

# Define parameters for the .wav file format
# Define parameters for the .wav file format
n_channels = 2
sample_width = 2
frame_rate = 44100
time_in_sec = 5
n_frames = frame_rate * time_in_sec
compression = 'NONE'
comp_name = 'none'
parameters = (n_channels, sample_width, frame_rate, n_frames, compression, comp_name)

first_note = 'Gb1'
first_freq = NN.find_freq(first_note)
print("The first note is {}. It\'s frequency is {}.".format(first_note, first_freq))


first_voice = ND.Voice('line','lhre', 24, 0.5, 13, 0.1, 1, 0.1)

first_base = NW.Base(first_freq, 24, 'harm', 'zero')

first_generator = NW.Generator(first_base, first_voice)
first_note = first_generator.build_wave(first_note, 5.0, frame_rate)

first_note = NZ.add_zero_noise(first_note,g=0.001)

#print(first_funfreq[0:1000])
first_note = NC.make_wave_positive(first_note)
first_note = NC.merge_stereo_chunk(first_note, first_note)
sample = NC.make_sample(first_note)

samp = wave.open('Neuro_wave1.wav','wb')
samp.setparams(parameters)
samp.writeframes(bytearray(sample))
samp.close()

#sample = wave.open('Neuro_wave1.wav','wb')
#sample.setparams(parameters)
#sample.writeframes(bytearray(score))
#sample.close()
