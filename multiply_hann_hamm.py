#!/usr/bin/python3

import sys
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import colors

#setting
extend_times= 3
minus_step = 9
frequency = 4
total_time = 1
res = 0.01

def plot_data(x_data, y_data, x_label, y_label, fig_name, title='Sine Wave', y_lim=None, plot_type='plot'):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_xlim(x_data[0], x_data[-1])
	if y_lim != None:
		ax.set_ylim(y_lim[0], y_lim[1])
	ax.set_ylabel(y_label)
	ax.set_xlabel(x_label)
	if plot_type == 'plot':
		ax.plot(x_data, y_data)
	elif plot_type == 'stem':
		ax.stem(x_data, y_data)
	ax.set_title(title)
	fig.savefig(fig_name)
	plt.close(fig)

def hann(total_data):
	hann_array = np.zeros(total_data)
	for i in range(total_data):
		hann_array[i] = 0.5 - 0.5 * np.cos((2 * np.pi * i) / (total_data - 1))
	return hann_array

def hamm(total_data):
	hann_array = np.zeros(total_data)
	for i in range(total_data):
		hann_array[i] = 0.5386 - 0.46164 * np.cos((2 * np.pi * i) / (total_data - 1))
	return hann_array

time = np.arange(0, total_time, res)
amplitude = np.sin(2 * np.pi * frequency * total_time * (time/time[-1]))

#modify
time = time[:-minus_step]
amplitude = amplitude[:-minus_step]

hann_weight = hann(len(amplitude))
hamm_weight = hamm(len(amplitude))

amplitude_multiplied_hann = amplitude * hann_weight
amplitude_multiplied_hamm = amplitude * hamm_weight

plot_data(time, amplitude_multiplied_hann, 'Time', 'Amplitude', 'Hann_multiplied_plot.png', 'Unfinished 4 Hz Sine Wave Weighted by Hann')
plot_data(time, amplitude_multiplied_hamm, 'Time', 'Amplitude', 'Hamm_multiplied_plot.png', 'Unfinished 4 Hz Sine Wave Weighted by Hamm')

#apply fft
fftdata_hann = np.fft.fft(amplitude_multiplied_hann)
fftdata_hamm = np.fft.fft(amplitude_multiplied_hamm)
fftdatafreq_hann = np.zeros(len(amplitude_multiplied_hann))
fftdatafreq_hamm = np.zeros(len(amplitude_multiplied_hamm))
for i in range(len(fftdata_hann)):
	fftdatafreq_hann[i] = abs(fftdata_hann[i].real)
	fftdatafreq_hamm[i] = abs(fftdata_hamm[i].real)

plot_data(np.arange(0, len(time) // 2), fftdatafreq_hann[:len(fftdatafreq_hann) // 2], 'Frequency', 'Power', 'Hann_multiplied_fft.png', 'FFT of Unfinished 4 Hz Sine Wave Weighted by Hann', y_lim=[0,20], plot_type='stem')
plot_data(np.arange(0, len(time) // 2), fftdatafreq_hamm[:len(fftdatafreq_hamm) // 2], 'Frequency', 'Power', 'Hamm_multiplied_fft.png', 'FFT of Unfinished 4 Hz Sine Wave Weighted by Hamm', y_lim=[0,20], plot_type='stem')
