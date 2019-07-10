
import wave #reading and writing .wav files
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import gamma
import NeuroLib as NL

# Define parameters for the .wav file format
n_channels = 2
sample_width = 4
frame_rate = 44100
time_in_sec = 5
n_frames = frame_rate * time_in_sec
compression = 'NONE'
comp_name = 'none'
parameters = (n_channels, sample_width, frame_rate, n_frames, compression, comp_name)

first_note = 'C1'
first_freq = NL.find_freq(first_note)
print("The first note is {}. It\'s frequency is {}.".format(first_note, first_freq))

first_series = NL.harmonic_series(first_freq, 6)
first_inv_series = NL.inv_harmonic_series(first_freq, 6)

print(first_series)
print(first_inv_series)

# create a sinewave
#  def sine_wave (amp,funf,phase,length,rate):
first_funfreq = NL.sine_wave(50,first_freq,0,44100,44100)
#print(first_funfreq[0:100])

# create a harmonic_base
# (funf, nharm, frate, dur, phase ):
first_base = NL.harmonic_base(first_freq,12,44100,5,0)
#print(first_base[0:50,0:50])

# linear_adsr(base, ai, at, bt, ba, ct)
#second_base = NL.geometric_overtones(first_base, 1, 0.5)
second_base = NL.equal_overtones(first_base)
#print(second_base[0,0:500])

modX, modY = NL.model_adsr( 0.0, 0.25, 0.5, 0.5, 0.95)
adsr_fig = plt.figure()
plt.plot(modX,modY)
adsr_fig.savefig('adsr_mod.png')

third_base = NL.linear_adsr(second_base, 0.0, 0.25, 0.5, 0.5, 0.95)
#print(third_base[0,0:500])

home_plate = NL.compile_overtones(third_base)
#print(home_plate)
print(max(home_plate))
score = NL.merge_stereo_chunk(home_plate, home_plate)
print(min(score))

score = NL.make_wave_positive(score)


sample = wave.open('Neuro_wave1.wav','wb')
sample.setparams(parameters)
sample.writeframes(bytearray(score))
sample.close()
