#!/usr/bin/python3

import sys
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import colors

#setting
extend_times= 3
minus_step = 5
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

time_extended = np.arange(0, total_time*extend_times, res)
amplitude_extended = np.zeros(len(amplitude)*extend_times)
for i in range(extend_times):
	amplitude_extended[i*len(amplitude):(i+1)*len(amplitude)] = amplitude

#print(amplitude_extended)
plot_data(time_extended, amplitude_extended, 'Time', 'Amplitude', 'sin_wave-extended.png', title='finished 4 Hz Sine Wave (Extended)')

#modified signal
time = time[:-minus_step]
amplitude = amplitude[:-minus_step]

time_modified_extended = np.arange(0, total_time*extend_times, res)[:-minus_step*extend_times]
amplitude_modified_extended = np.zeros(len(amplitude)*extend_times)
for i in range(extend_times):
	amplitude_modified_extended[i*len(amplitude):(i+1)*len(amplitude)] = amplitude
plot_data(time_modified_extended, amplitude_modified_extended, 'Time', 'Amplitude', 'test-3.png', title='unfinished 4 Hz Sine Wave (Extended)')

#apply fft
fftdata = np.fft.fft(amplitude_modified_extended)
fftdatafreq = np.zeros(len(amplitude_modified_extended))
for i in range(len(fftdata)):
	fftdatafreq[i] = abs(fftdata[i].real)

plot_data(np.arange(0, len(time_modified_extended) // 2), fftdatafreq[:len(time_modified_extended) // 2], 
'Frequency', 'Power', 'sin_wave_fft-modified-extended.png', title='FFT of Unfinished 4 Hz Sine Wave (extended)', y_lim=20)
