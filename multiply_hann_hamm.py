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

def plot_data(x_data, y_data, x_label, y_label, fig_name, title='Sine Wave', y_lim=None, ):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_xlim(x_data[0], x_data[-1])
	if y_lim != None:
		ax.set_ylim(-y_lim, y_lim)
	ax.set_ylabel(y_label)
	ax.set_xlabel(x_label)
	ax.plot(x_data, y_data)
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

amplitude = np.sin(2 * np.pi * frequency * (time/time[-1]))
amplitude = amplitude[:-minus_step]

time_modified_extended = np.arange(0, total_time*extend_times, res)[:-minus_step*extend_times]
amplitude_modified_extended = np.zeros(len(amplitude)*extend_times)
for i in range(extend_times):
	amplitude_modified_extended[i*len(amplitude):(i+1)*len(amplitude)] = amplitude

hann_weight = hann(len(amplitude_modified_extended))
hamm_weight = hamm(len(amplitude_modified_extended))

amplitude_modified_extended_hann = amplitude_modified_extended * hann_weight
amplitude_modified_extended_hamm = amplitude_modified_extended * hamm_weight

print(amplitude_modified_extended_hann)

plot_data(time_modified_extended, amplitude_modified_extended_hann, 'Time', 'Amplitude', 'Hann_multiplied_plot.png', 'Unfinished 4 Hz Sine Wave Weighted by Hann', y_lim=1)
plot_data(time_modified_extended, amplitude_modified_extended_hamm, 'Time', 'Amplitude', 'Hamm_multiplied_plot.png', 'Unfinished 4 Hz Sine Wave Weighted by Hamm', y_lim=1)
