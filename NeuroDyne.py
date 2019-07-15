
# Neuro Envelope Library
# This module contains a collection of Neurowave
# trigger, envelope, and other amplitude controls


import math
import wave #reading and writing .wav files
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma
import NeuroLib as NL
import NeuroConstruct as NC
import NeuroNoise as NZ
import NeuroNote as NN
import NeuroWave as NW

class Voice:

    def __init__(self, envm, harm, *params):
        envm = '_' + envm
        harm = '_' + harm
        if envm in env_lib.keys():
            self.env_model = env_lib[envm]
        else:
            print("Envelope model {} not found. Using default type: \'linear\'".format(envm))
        if harm in harm_lib.keys():
            self.har_model = harm_lib[harm]
        else:
            print("Harmonic model {} not found. Using default type: \'linear\'".format(harm))
        self.parameters = params
        self.env_set = self.build_env_set()

    def build_env_set(self):
        env_set = self.har_model(self.env_model,self.parameters)
        return(env_set)

    def print_env_set(self):
        print(self.env_set)


class Envelope:

    def __init__(self,etype='line'):
        etype = '_' + etype
        if etype in env_lib.keys():
            self.etype = env_lib[etype]
        else:
            print("Envelope of type {} not found. Using default type: \'line\'".format(type))

    def calc_envelope(self, time, params):
        env = self.etype(time, params)
        return(env)

lenvelopes = np.array([
    [20,5],[10,1],[17,5],[7,1],
    [13,5],[5,1],[10,5],[2,1],
    [5,5],[2,1],[5,5],[2,1],
    [3,1],[2,1],[3,0.9],[2,0.8],
    [3,0.7],[2,0.6],[3,0.5],[3,0.4],
    [3,0.3],[2,0.2],[3,0.1],[2,0],
])



def envelope_adsr(time, x):
    """ Calclate an ADSR (attack, decay, sustain, release) envelope
        to based on t to mold the general shape of a sound
        t is a numpy array, the envelope function will return an
        int for the amplitude at t based on the model
        times are specified as sample quantitites
        at = attack time, aa = attack amplitude, ai = amplitude intercept
        bt = decay time, ba = decay amplitude, ct = sustain time, dt = decay time
    """
    ai, at, aa, bt, ba, ct, dt = x[0:7]

    amp = np.zeros(len(time))

    for t in time:
        if t < 0 :
            amp[int(t)] = 0
        elif t >= 0 and t <= at :
            amp[int(t)] = ai + (aa - ai) / at * t
        elif t > at and t <= bt :
            amp[int(t)] = aa + ( ba - aa ) / ( bt - at ) * ( t - at )
        elif t > bt and t <= ct :
            amp[int(t)] = ba
        elif t > ct and t <= dt :
            amp[int(t)] = ba * ( (ct - t) / (dt - ct) + 1 )
        elif t > dt :
            amp[int(t)] = 0
        else:
            print("Problem calculating asdr. Index {} not in adsr's domain.".format(x))
            return

    return(amp)

def envelope_linear(time,c):
    """ Calcuate amplitude for simple linear envelope model
    """
    #print(c)
    amp = np.zeros(len(time))
    a, b = c[0:2]
    for t in time:

        amp[int(t)] = int( a + (b - a) / len(time) * t )

    return(amp)

def manual_voice(*a):
    for i in a:
        pass
    return(a)

def linear_harmonics(n, m):
    a, b, y, z = m[1:5]
    lh = np.zeros((m[0],2))
    for i in range(0,m[0],1):
        lh[i][0] = a + ( b - a ) / m[0] * i
        lh[i][1] = y + ( z - y ) / m[0] * i
    return(lh)

def linear_harmonics_red_even(n, m):
    r, a, b, y, z = m[1:6]
    lh = np.zeros((m[0],2))
    for i in range(0,m[0],1):
        if i % 2 == 0:
            lh[i][0] = r * ( a + ( b - a ) / m[0] * i )
            lh[i][1] = r * ( y + ( z - y ) / m[0] * i )
        else:
            lh[i][0] = a + ( b - a ) / m[0] * i
            lh[i][1] = y + ( z - y ) / m[0] * i
    return(lh)


env_lib = {
     '_adsr' : envelope_adsr,
     '_line' : envelope_linear
}

voice_lib = {
    '_manu' : manual_voice
}

harm_lib = {
    '_line' : linear_harmonics,
    '_lhre' : linear_harmonics_red_even
}
