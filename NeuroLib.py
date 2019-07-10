
# This is a python library for use with
# NeuroWave synthwave generator and song engine
#

import math
import wave #reading and writing .wav files
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# make function that computes a sine wave
def sine_wave (amp,funf,phase,length,rate):
    """ Generate a list containing data for a sinewave
        a = amplitude, f = frequency in Hz, p = phase of sine function,
        l = number of samples, r = sampling rate (samples/sec)
    """
    wave_data = np.zeros(length, dtype=int)
    for i in range(0,length,1):
        y = amp * math.sin(2 * math.pi * funf * i/rate + phase)
        wave_data[i]= int(y)
    return wave_data

note_bank = {
""" Note bank is a dictionary storing the fundamental frequencies
    of the notes found on a piano with an extended range of +/-
    one octave
"""
'A0'  : 27.50000,
'Bb0' : 29.13524,
'B0'  : 30.86771,
'C1'  : 32.70320,
'Db1' : 34.64783,
'D1'  : 36.70810,
'Eb1' : 38.89087,
'E1'  : 41.20344,
'F1'  : 43.65353,
'Gb1' : 46.24930,
'G1'  : 48.99943,
'Ab1' : 51.91309,
'A1'  : 55.00000,
'Bb1' : 58.27047,
'B1'  : 61.73541,
'C2'  : 65.40639,
'Db2' : 69.29566,
'D2'  : 73.41619,
'Eb2' : 77.78175,
'E2'  : 82.40689,
'F2'  : 87.30706,
'Gb2' : 92.49861,
'G2'  : 97.99886,
'Ab2' : 103.8262,
'A2'  : 110.0000,
'Bb2' : 116.5409,
'B2'  : 123.4708,
'C3'  : 130.8128,
'Db3' : 138.5913,
'D3'  : 146.8324,
'Eb3' : 155.5635,
'E3'  : 164.8138,
'F3'  : 174.6141,
'Gb3' : 184.9972,
'G3'  : 195.9977,
'Ab3' : 207.6523,
'A3'  : 220.0000,
'Bb3' : 233.0819,
'B3'  : 246.9417,
'C4'  : 261.6256,
'Db4' : 277.1826,
'D4'  : 293.6648,
'Eb4' : 311.1270,
'E4'  : 329.6276,
'F4'  : 249.2282,
'Gb4' : 369.9944,
'G4'  : 391.9954,
'Ab4' : 415.3047,
'A4'  : 440.0000,
'Bb4' : 466.1638,
'B4'  : 493.8833,
'C5'  : 523.2511,
'Db5' : 554.3653,
'D5'  : 587.3295,
'Eb5' : 622.2540,
'E5'  : 659.2551,
'F5'  : 698.4565,
'Gb5' : 739.9888,
'G5'  : 783.9909,
'Ab5' : 830.6094,
'A5'  : 880.0000,
'Bb5' : 932.3275,
'B5'  : 987.7666,
'C6'  : 1046.502,
'Db6' : 1108.731,
'D6'  : 1174.659,
'Eb6' : 1244.508,
'E6'  : 1318.510,
'F6'  : 1396.913,
'Gb6' : 1479.978,
'G6'  : 1567.982,
'Ab6' : 1661.219,
'A6'  : 1760.000,
'Bb6' : 1864.655,
'B6'  : 1975.533,
'C7'  : 2093.005,
'Db7' : 2217.461,
'D7'  : 2349.318,
'Eb7' : 2489.016,
'E7'  : 2637.020,
'F7'  : 2793.826,
'Gb7' : 2959.955,
'G7'  : 3135.963,
'Ab7' : 3322.438,
'A7'  : 3520.000,
'Bb7' : 3729.310,
'B7'  : 3951.066,
'C8'  : 4186.009,
'B8'  : 7902.133,
'Bb8' :	7458.620,
'A8'  : 7040.000,
'Ab8' :	6644.875,
'G8'  : 6271.927,
'Gb8' : 5919.911,
'F8'  : 5587.652,
'E8'  : 5274.041,
'Eb8' :	4978.032,
'D8'  : 4698.636,
'Db8' : 4434.922,
'Ab0' : 25.95654,
'G0'  : 24.49971,
'Gb0' : 23.12465,
'F0'  :	21.82676,
'E0'  : 20.60172,
'Eb0' :	19.44544,
'D0'  :	18.35405,
'Db0' :	17.32391,
'C0'  :	16.35160
}

# find_freq will find and return the frequency from
# the note_bank
def find_freq(note):
    """ takes a string name for the note, e.g. 'C4'
    and returns the frequency """
    frequency = note_bank[note]
    return frequency

def harmonic_series(f,n):
    """ compute the first n frequencies in a harmonic series
        from a given frequency f
    """
    series = [f]
    for i in range(1,n,1):
        series.append(f * (i + 1))
    return(series)

def inv_harmonic_series(f,n):
    """ compute the first n frequencies in an inverted harmonic
        series from a given frequency f
    """
    series = [f]
    for i in range(1,n,1):
        series.append(f / (i + 1))
    return(series)

def harmonic_base(funf, nharm, frate, dur, phase ):
    """ make a synth note
        create a numpy 2D array storing nharm sinewaves for a given
        harmonic series based on a:
        fundamental frequency f
        frate = frame rate (smaples per second)
        dur = duration in seconds
        phase = a list of phase shift valuse, length must be 1 or
        equal to nharm
    """
    # check the phase list for =nharm or 1, return if neither
    phase = [phase]
    if len(phase) == 1:
        phase = [phase[0] for i in range(0,nharm,1)]
    elif len(phase) != nharm:
        print("Cannot synthesize base! Length of phase list must equal the number of harmonics or equal 1.")
        return
    else:
        pass

    # set the base amplitude and calculate the number of samples needed (length)
    amp = 128
    length = frate * dur
    # initialize a base 2D array
    base = np.zeros((nharm, length), dtype=int)

    for i in range(0,nharm,1):
        wave = sine_wave(amp,funf,phase[i],length,frate)
        for j in range(0,length,1):
            base[i,j] = wave[j]

    return(base)

def linear_attack(ai,at,t):
    """ returns the value for t of a linear attack model
    """
    return( ai + ( 1 - ai ) / at * t )

def linear_decay(ba, bt, at, t ):
    """ returns the value for t of a linear decay model
    """
    return( ba + ( ba - 1 ) / ( bt - at ) * ( t - bt ) )

def linear_release(ba, ct, dt, t):
    """ returns the value for t of a linear release model
    """
    #( t + 1 ) * ( (-ba) / ( dt - ct ) )
    return( ba * ( (ct - t) / (dt - ct) + 1 ) )

def geometric_overtones(base, a, r):
    """ Use a geometric series to reduce harmonic overtones
    """

    # calculate integers to address where phases of the model switch
    time = range(0,base.shape[1],1)
    harm = range(0,base.shape[0],1)

    for i in time:
        for j in harm:
            base[j,i] = base[j,i] * a*(r**(j+1))
            #print(a*(r**(j+1)))

    return(base)

def make_wave_positive(base):
    """ make all harmonic overtones equal
    """

    # calculate integers to address where phases of the model switch
    time = range(0,len(base),1)
    a = min(base)
    if a < 0:
        a = -a
    else:
        print("Wave is already positive.")
        return

    for i in time:
        base[i] = base[i] + a

    return(base)

def equal_overtones(base):
    """ make all harmonic overtones equal
    """

    # calculate integers to address where phases of the model switch
    time = range(0,base.shape[1],1)
    harm = range(0,base.shape[0],1)

    for i in time:
        for j in harm:
            base[j,i] = base[j,i] / len(harm)
            #print(a*(r**(j+1)))

    return(base)

def compile_overtones(base):
    """ sum over overtones to create a single wave form
    """
    # calculate integers to address where phases of the model switch
    time = range(0,base.shape[1],1)
    harm = range(0,base.shape[0],1)

    wave = np.zeros(base.shape[1], dtype=int)

    for i in time:
        sample = 0
        for j in harm:
            sample += base[j,i]

        wave[i] = int(sample)

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

    return(chunk)

def linear_adsr(base, ai, at, bt, ba, ct):
    """ Apply an ADSR (attack, decay, sustain, release) model
        to a harmonic base to mold the general shape of a sound
        parameters are given as propotions of the domain they affect,
        either amplitude or time
        at = attack time, aa = attack amplitude, ai = amplitude intercept
        bt = decay time, ba = decay amplitude, ct = sustain time
    """

    # calculate integers to address where phases of the model switch
    time = range(0,base.shape[1],1)
    harm = range(0,base.shape[0],1)
    at = int(round( len(time) * at, 0 ))
    bt = int(round( len(time) * bt, 0 ))
    ct = int(round( len(time) * ct, 0 ))
    dt = len(time)

    # do the same with the amplitude parameters
    max_amp = np.max(base)
    aa = 1.0
    da = 0

    # establish ranges for the modes
    attack_range = range(0,at,1)
    decay_range = range(at,bt,1)
    sustain_range = range(bt,ct,1)
    release_range = range(ct,dt+1,1)
    #print("{} {} | {} {} | {} {} | {} {}".format(min(attack_range),max(attack_range),min(decay_range),max(decay_range),min(sustain_range),max(sustain_range),min(release_range),max(release_range)))

    for i in harm:
        for j in time:
            if j in attack_range:
                base[i,j] = base[i,j] * linear_attack(ai,at,j)
            elif j in decay_range:
                base[i,j] = base[i,j] * linear_decay(ba, bt, at, j)
            elif j in sustain_range:
                base[i,j] = base[i,j] * ba
            elif j in release_range:
                base[i,j] = base[i,j] * linear_release(ba, ct, dt, j)
            else:
                print("Problem calculating asdr. Index {} not in base range.".format(j))
                return

    return(base)

def model_adsr(ai, at, bt, ba, ct):
    """ Model an ADSR (attack, decay, sustain, release) model
        to a harmonic base to mold the general shape of a sound
        parameters are given as propotions of the domain they affect,
        either amplitude or time
        at = attack time, aa = attack amplitude, ai = amplitude intercept
        bt = decay time, ba = decay amplitude, ct = sustain time
    """

    # calculate integers to address where phases of the model switch
    time = np.array(range(0,1000,1))
    amplitude = np.zeros(1000)

    at = int(round( len(time) * at, 0 ))
    bt = int(round( len(time) * bt, 0 ))
    ct = int(round( len(time) * ct, 0 ))
    dt = len(time)

    # do the same with the amplitude parameters
    aa = 1.0
    da = 0

    # establish ranges for the modes
    attack_range = range(0,at,1)
    decay_range = range(at,bt,1)
    sustain_range = range(bt,ct,1)
    release_range = range(ct,dt+1,1)

    for j in time:
        if j in attack_range:
            amplitude[j] = linear_attack(ai,at,j)
        elif j in decay_range:
            amplitude[j] = linear_decay(ba, bt, at, j)
        elif j in sustain_range:
            amplitude[j] = ba
        elif j in release_range:
            amplitude[j] = linear_release(ba, ct, dt, j)
        else:
            print("Problem calculating asdr. Index {} not in base range.".format(j))
            return

    return([time, amplitude])
