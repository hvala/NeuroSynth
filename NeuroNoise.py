
# NeuroNoise
# Neuro Noise is a module for adding noise and sound FX
# to Neuro Synth sounds

import math
import wave #reading and writing .wav files
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma
import NeuroLib as NL
import NeuroConstruct as NC
import NeuroNote as NN
import NeuroWave as NW
import NeuroDyne as ND


def add_gaussian_noise(x, noise=1.0):
    """ add noise to a wave using random draws from a normal/gaussian distribution
    """

    for i in range(0,len(x),1):
        x[i] = int(np.random.normal(loc=x[i], scale=noise, size=1))

    return(x)

def add_wsample_noise(x, noise=1.0, g=0.01):
    """ add noise to a wave using random draws from a normal/gaussian distribution
    """

    for i in range(0,len(x),1):
        r = np.random.random(1)
        w = x[0]
        gap = 1.0 - g
        if r <= gap:
            pass
            #x[i] = int(np.random.normal(loc=x[i], scale=noise, size=1))
        elif r > gap and r <= gap + 0.5 * g :
            x[i] = w
        else:
            w = x[i]
            #x[i] = int(np.random.normal(loc=x[i], scale=noise, size=1))

    return(x)

def add_choice_noise(x, g=0.01):
    """ add noise to a wave using random draws from a normal/gaussian distribution
    """
    gap = 1.0 - g
    for i in range(0,len(x),1):
        r = np.random.random(1)
        if r <= gap:
            pass
            #x[i] = int(np.random.normal(loc=x[i], scale=noise, size=1))
        else:
            x[i] = np.random.choice(x,1)

    return(x)

def add_zero_noise(x, g=0.01):
    """ add noise to a wave using random draws from a normal/gaussian distribution
    """
    gap = 1.0 - g
    for i in range(0,len(x),1):
        r = np.random.random(1)
        if r <= gap:
            pass
            #x[i] = int(np.random.normal(loc=x[i], scale=noise, size=1))
        else:
            x[i] = 0

    return(x)
