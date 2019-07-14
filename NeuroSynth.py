
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

first_note = 'E2'
first_freq = NN.find_freq(first_note)
print("The first note is {}. It\'s frequency is {}.".format(first_note, first_freq))

first_series = NW.harmonic_series(first_freq, 6)
first_inv_series = NW.inv_harmonic_series(first_freq, 6)

print(first_series)
print(first_inv_series)

#def envelope_adsr(t, ai, at, aa, bt, ba, ct, dt):
envelopes = np.array([
    [0, NC.nsamples(0.001), 12, NC.nsamples(4.0), 5, NC.nsamples(4.01), NC.nsamples(5.0)],
    [0, NC.nsamples(0.001), 10, NC.nsamples(4.0), 5, NC.nsamples(4.01), NC.nsamples(5.0)],
    [0, NC.nsamples(0.001), 8,  NC.nsamples(4.0), 4, NC.nsamples(4.01), NC.nsamples(5.0)],
    [0, NC.nsamples(0.001), 7,  NC.nsamples(4.0), 3, NC.nsamples(4.01), NC.nsamples(5.0)],
    [0, NC.nsamples(0.001), 6,  NC.nsamples(4.0), 2, NC.nsamples(4.01), NC.nsamples(5.0)],
    [0, NC.nsamples(0.001), 5,  NC.nsamples(4.0), 1, NC.nsamples(4.01), NC.nsamples(5.0)],
    [0, NC.nsamples(0.001), 2,  NC.nsamples(4.0), 1, NC.nsamples(4.01), NC.nsamples(5.0)],
    [0, NC.nsamples(0.001), 2,  NC.nsamples(4.0), 1, NC.nsamples(4.01), NC.nsamples(5.0)],
    [0, NC.nsamples(0.001), 0.1,  NC.nsamples(4.0), 1, NC.nsamples(4.01), NC.nsamples(5.0)],
    [0, NC.nsamples(0.001), 0.1,  NC.nsamples(4.0), 1, NC.nsamples(4.01), NC.nsamples(5.0)],
    [0, NC.nsamples(0.001), 0.1,  NC.nsamples(4.0), 1, NC.nsamples(4.01), NC.nsamples(5.0)],
    [0, NC.nsamples(0.001), 0.1,  NC.nsamples(4.0), 1, NC.nsamples(4.01), NC.nsamples(5.0)]
    ])

lenvelopes = np.array([
    [17,1],[20,1],[12,1],[2,1],
    [6.0,1],[1.0,1],[4,1],[0.2,0.1],
    [0.5,0.1],[0.2,0.1],[0.5,0.1],[0.2,0.1],
    [0.1,0.1],[0.1,0.1],[0.1,0.1],[2,0.1],
    [0.1,0.1],[0.1,0.1],[0.1,0.1],[0.1,0.1],
    [0.1,0.1],[0.1,0.1],[0.1,0.1],[0.1,0.1],
])

first_voice = ND.Voice('line','line', 24, 20, 0.1, 1, 0.1)
#first_voice.print_env_set()

first_base = NW.Base(first_freq, 24, 'harm', 'zero')
first_base.print_phase_set()
first_base.print_harm_set()

#modX = np.linspace(0,NC.nsamples(5.0),NC.nsamples(5.0)+1)
#modY = ND.envelope_adsr( modX, envelopes[11])
#adsr_fig = plt.figure()
#plt.plot(modX,modY)
#adsr_fig.savefig('adsr_mod.png')


amps = (10, 12, 8, 7, 6, 5, 1, 1, 1, 1, 1, 1)
phis = (0,0,0,0,0,0,
        0,0,0,0,0,0,
        0,0,0,0,0,0,
        0,0,0,0,0,0)
# create a sinewave
#  def sine_wave (amp,funf,phase,length,rate):
first_funfreq = NW.harmonic_wave(first_freq,24,phis,time_in_sec,frame_rate,'line',lenvelopes)


#add some noise
#first_funfreq = NZ.add_zero_noise(first_funfreq,g=0.05)

#print(first_funfreq[0:1000])
first_funfreq = NC.make_wave_positive(first_funfreq)
first_funfreq = NC.merge_stereo_chunk(first_funfreq, first_funfreq)
sample = NC.make_sample(first_funfreq)

samp = wave.open('Neuro_wave1.wav','wb')
samp.setparams(parameters)
samp.writeframes(bytearray(sample))
samp.close()

#sample = wave.open('Neuro_wave1.wav','wb')
#sample.setparams(parameters)
#sample.writeframes(bytearray(score))
#sample.close()
