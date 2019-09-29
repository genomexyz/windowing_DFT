#!/usr/bin/python3

import sys
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import colors

#setting
minus_step = 9
frequency = 4
total_time = 1
res = 0.01

def plot_data(x_data, y_data, x_label, y_label, fig_name, title='Sine Wave', y_lim=None):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_xlim(x_data[0], x_data[-1])
	if y_lim != None:
		ax.set_ylim(0, y_lim)
	ax.set_ylabel(y_label)
	ax.set_xlabel(x_label)
	ax.stem(x_data, y_data)
	ax.set_title(title)
	fig.savefig(fig_name)
	plt.close(fig)

time = np.arange(0, total_time, res)
amplitude = np.sin(2 * np.pi * frequency * total_time * (time/time[-1]))

plot_data(time, amplitude, 'Time', 'Amplitude', 'sin_wave.png', title='4 Hz Sine Wave')


#apply fft
fftdata = np.fft.fft(amplitude)
fftdatafreq = np.zeros(len(amplitude))
for i in range(len(fftdata)):
	fftdatafreq[i] = abs(fftdata[i].real)

plot_data(np.arange(0, len(time) // 2), fftdatafreq[:len(time) // 2], 
'Frequency', 'Power', 'sin_wave_fft.png', title='FFT of 4 Hz Sine Wave', y_lim=20)

#modify
time = time[:-minus_step]
amplitude = amplitude[:-minus_step]

plot_data(time, amplitude, 'Time', 'Amplitude', 'sin_wave-modified.png', title='Unfinished 4 Hz Sine Wave')

#apply fft
fftdata = np.fft.fft(amplitude)
fftdatafreq = np.zeros(len(amplitude))
for i in range(len(fftdata)):
	fftdatafreq[i] = abs(fftdata[i].real)

plot_data(np.arange(0, len(time) // 2), fftdatafreq[:len(time) // 2], 'Frequency', 
'Power', 'sin_wave-modified_fft.png', title='FFT of Unfinished 4 Hz Sine Wave', y_lim=20)
