
import wave #reading and writing .wav files
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import gamma
import scipy.io.wavfile as spw
import NeuroLib as NL

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

first_note = 'C4'
first_freq = NL.find_freq(first_note)
print("The first note is {}. It\'s frequency is {}.".format(first_note, first_freq))

first_series = NL.harmonic_series(first_freq, 6)
first_inv_series = NL.inv_harmonic_series(first_freq, 6)

print(first_series)
print(first_inv_series)

#def envelope_adsr(t, ai, at, aa, bt, ba, ct, dt):
envelopes = np.array([
    [0, NL.nsamples(0.001), 12, NL.nsamples(4.0), 5, NL.nsamples(4.01), NL.nsamples(5.0)],
    [0, NL.nsamples(0.001), 10, NL.nsamples(4.0), 5, NL.nsamples(4.01), NL.nsamples(5.0)],
    [0, NL.nsamples(0.001), 8,  NL.nsamples(4.0), 4, NL.nsamples(4.01), NL.nsamples(5.0)],
    [0, NL.nsamples(0.001), 7,  NL.nsamples(4.0), 3, NL.nsamples(4.01), NL.nsamples(5.0)],
    [0, NL.nsamples(0.001), 6,  NL.nsamples(4.0), 2, NL.nsamples(4.01), NL.nsamples(5.0)],
    [0, NL.nsamples(0.001), 5,  NL.nsamples(4.0), 1, NL.nsamples(4.01), NL.nsamples(5.0)],
    [0, NL.nsamples(0.001), 2,  NL.nsamples(4.0), 1, NL.nsamples(4.01), NL.nsamples(5.0)],
    [0, NL.nsamples(0.001), 2,  NL.nsamples(4.0), 1, NL.nsamples(4.01), NL.nsamples(5.0)],
    [0, NL.nsamples(0.001), 2,  NL.nsamples(4.0), 1, NL.nsamples(4.01), NL.nsamples(5.0)],
    [0, NL.nsamples(0.001), 2,  NL.nsamples(4.0), 1, NL.nsamples(4.01), NL.nsamples(5.0)],
    [0, NL.nsamples(0.001), 2,  NL.nsamples(4.0), 1, NL.nsamples(4.01), NL.nsamples(5.0)],
    [0, NL.nsamples(0.001), 2,  NL.nsamples(4.0), 1, NL.nsamples(4.01), NL.nsamples(5.0)]
    ])

lenvelopes = np.array([
    [20,5],[10,1],[17,5],[7,1],
    [13,5],[5,1],[10,5],[2,1],
    [5,5],[2,1],[5,5],[2,1],
    [3,1],[2,1],[3,0.9],[2,0.8],
    [3,0.7],[2,0.6],[3,0.5],[3,0.4],
    [3,0.3],[2,0.2],[3,0.1],[2,0],
])

modX = np.linspace(0,NL.nsamples(5.0),NL.nsamples(5.0)+1)
modY = NL.envelope_adsr( modX, envelopes[11])
adsr_fig = plt.figure()
plt.plot(modX,modY)
adsr_fig.savefig('adsr_mod.png')


amps = (10, 12, 8, 7, 6, 5, 1, 1, 1, 1, 1, 1)
phis = (0, 0.1, 0, 0.2, 0, 0.3, 0, 0.4, 0, 0.5, 0, 0.5, 0, 0.7, 0, 0.8, 0, 0.9, 0, 1.0, 0, 1.1, 0, 1.2)
# create a sinewave
#  def sine_wave (amp,funf,phase,length,rate):
first_funfreq = NL.harmonic_linenv_wave(lenvelopes,first_freq,24,phis,time_in_sec,frame_rate)


#add some noise
#first_funfreq = NL.add_zero_noise(first_funfreq,g=0.05)

#print(first_funfreq[0:1000])
first_funfreq = NL.make_wave_positive(first_funfreq)


first_funfreq = NL.merge_stereo_chunk(first_funfreq, first_funfreq)

print(type(first_funfreq))

sample = list()
for i in range(0,len(first_funfreq),1):
    sample.append(int(round(first_funfreq[i],0)))


samp = wave.open('Neuro_wave1.wav','wb')
samp.setparams(parameters)
samp.writeframes(bytearray(sample))
samp.close()

#sample = wave.open('Neuro_wave1.wav','wb')
#sample.setparams(parameters)
#sample.writeframes(bytearray(score))
#sample.close()
