import tensorflow as tf
import math
from scipy import signal
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import pylab

filename = "eight"
filepath = "C:/Users/tnordahl/Desktop/tensorflow_datasets/speech_commands_v0.01/eight/68dd409e_nohash_0.wav"
sample_rate2, samples = wavfile.read(filepath)

def log_specgram(audio, sample_rate, window_size=20,step_size=10, eps=1e-10):

    nperseg = int(round(window_size * sample_rate / 1e3))
    noverlap = int(round(step_size * sample_rate / 1e3))
    freqs, times, spec = signal.spectrogram(audio,
                                    fs=sample_rate,
                                    window='hann',
                                    nperseg=nperseg,
                                    noverlap=noverlap,
                                    detrend=False)
    return freqs, times, np.log(spec.T.astype(np.float32) + eps)

freqs, times, spectrogram = log_specgram(samples, sample_rate2)

fig = plt.figure(figsize=(14, 8))
ax1 = fig.add_subplot(211)
ax1.set_title('Raw wave of ' + filename)
ax1.set_ylabel('Amplitude')
ax1.plot(np.linspace(0, sample_rate2/len(samples), sample_rate2), samples)


ax2 = fig.add_subplot(212)
ax2.imshow(spectrogram.T, aspect='auto', origin='lower',
           extent=[times.min(), times.max(), freqs.min(), freqs.max()])
ax2.set_yticks(freqs[::16])
ax2.set_xticks(times[::16])
ax2.set_title('Spectrogram of ' + filename)
ax2.set_ylabel('Freqs in Hz')
ax2.set_xlabel('Seconds')
pylab.show()

