from numpy.random import default_rng
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import wave
obj = wave.open('output1.wav')
rng = default_rng()
print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print('Frame rate', obj.getframerate())
print('Number of frames', obj.getnframes())

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)
obj.close()

t_audio = n_samples / sample_freq
print("Time", t_audio)