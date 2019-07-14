
# NeuroNote is module containing functions and objects
# for describing muscial notational concepts and
# and musical theoretical structures

import math
import wave #reading and writing .wav files
import numpy as np
import NeuroLib as NL
import NeuroConstruct as NC
import NeuroNoise as NZ
import NeuroNote as NN
import NeuroWave as NW
import NeuroDyne as ND

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
    return(frequency)

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
