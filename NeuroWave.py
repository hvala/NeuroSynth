
# NeuroWave is a library for NeuroSynth
# This module contains functions and classes used in the
# creation of wave forms

import math
import wave #reading and writing .wav files
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma
import NeuroLib as NL
import NeuroConstruct as NC
import NeuroNoise as NZ
import NeuroNote as NN
import NeuroDyne as ND



class Base:

    def __init__(self, fundf, nharm, harm, phase, addfreqs=None ):
        self.fundfreq = fundf
        self.nharmonics = nharm
        harm = '_' + harm
        if harm in series_lib.keys():
            self.harm_model = series_lib[harm]
        else:
            self.harm_series = series_lib['_harm']
            print("Harmonic series {} not found. Using default harmonic series.".format(harm))
        phase = "_" + phase
        if phase in phase_lib.keys():
            self.phase_model = phase_lib[phase]
        else:
            self.phase = phase_lib['_zero']
            print("Phase set {} not found. Using default phase set: _zero.".format(phase))
        self.phase_set = self.build_phase_set()
        self.harm_series = self.build_harm_set()

        if addfreqs != None:
            self.harm_series = self.harm_series + np.array(addfreqs)
            self.nharmonics += len(addfreqs)

    def build_phase_set(self):
        phase_set = self.phase_model(self.nharmonics)
        return(phase_set)

    def build_harm_set(self):
        harm_model = self.harm_model(self.fundfreq,self.nharmonics)
        return(harm_model)

    def print_phase_set(self):
        print(self.phase_set)
        return

    def print_harm_set(self):
        print(self.harm_series)
        return

# make function that computes a sine wave
def sine_wave (amp,funf,phase,length,rate):
    """ Generate a list containing data for a sinewave
        a = amplitude, f = frequency in Hz, p = phase of sine function,
        l = number of samples, r = sampling rate (samples/sec)
    """
    n_samples = length * rate
    time = np.linspace(0,n_samples,n_samples)
    wave_data = amp * np.sin(2 * math.pi * funf * time / rate + phase)
    return(wave_data)


# a function
# make function that computes a sine wave
def harmonic_wave (funf,n,phase,length,rate,envtype,envparams):
    """ Generate a list containing data for a sinewave
        a = amplitude, f = frequency in Hz, p = phase of sine function,
        l = number of samples, r = sampling rate (samples/sec)
    """
    n_samples = length * rate
    freqs = harmonic_series(funf,n)
    env = ND.Envelope(envtype)

    time = np.linspace(0,n_samples-1,n_samples)

    wave_data = np.zeros(n_samples)
    for i in range(0,len(freqs),1):
        wave_data += env.calc_envelope(time, envparams[i]) * np.sin(2 * math.pi * freqs[i]* time / rate + phase[i])

    return(wave_data)

# a function
# make function that computes a sine wave
def harmonic_adsr_wave (amp,funf,n,phase,length,rate):
    """ Generate a list containing data for a sinewave
        a = amplitude, f = frequency in Hz, p = phase of sine function,
        l = number of samples, r = sampling rate (samples/sec)
    """
    n_samples = NC.nsamples(length)
    freqs = harmonic_series(funf,n)

    time = np.linspace(0,n_samples-1,n_samples)

    wave_data = np.zeros(n_samples)
    for i in range(0,len(freqs),1):
        wave_data += ND.envelope_adsr(time, amp[i]) * ( np.sin(2 * math.pi * freqs[i]* time / rate + phase[i]) )

    return(wave_data)

# a function
# make function that computes a sine wave
def harmonic_linenv_wave (amp,funf,n,phase,length,rate):
    """ Generate a list containing data for a sinewave
        a = amplitude, f = frequency in Hz, p = phase of sine function,
        l = number of samples, r = sampling rate (samples/sec)
    """
    n_samples = NC.nsamples(length)
    freqs = harmonic_series(funf,n)

    time = np.linspace(0,n_samples-1,n_samples)

    wave_data = np.zeros(n_samples)
    for i in range(0,len(freqs),1):
        wave_data += ND.envelope_linear(time, amp[i]) * ( np.sin(2 * math.pi * freqs[i]* time / rate + phase[i]) )

    return(wave_data)


def harmonic_series(f,n):
    """ compute the first n frequencies in a harmonic series
        from a given frequency f
    """
    series = np.zeros(n)
    series[0] = f
    for i in range(1,n,1):
        series[i] = (f * (i + 1))
    return(series)

def inv_harmonic_series(f,n):
    """ compute the first n frequencies in an inverted harmonic
        series from a given frequency f
    """
    series = np.zeros(n)
    series[0] = f
    for i in range(1,n,1):
        series[i] = (f * (i + 1))
    return(series)

def phase_zero(n):
    return(np.zeros(int(n)))

series_lib = {
    '_harm' : harmonic_series,
    '_invh' : inv_harmonic_series
}

phase_lib = {
    '_zero' : phase_zero
}
