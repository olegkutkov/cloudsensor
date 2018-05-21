#!/usr/bin/python

import numpy as np

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import sqlite3

import config

def plot_cpu_temperature(sensor_data, output_file):
	xdata = []
	ydata = []

	print 'Plotting cpu temperature graph using ' + str(len(sensor_data)) + ' db records'

	for row in sensor_data:
		xdata.append(row[0])
		ydata.append(row[1])

	temper = np.array(ydata)

	plt.title('CPU temperature: ' + str(ydata[-1]) + ' C\n')
	plt.plot(xdata, temper, label = "Temperature", color="red")

	plt.xlabel('Time period: ' + str(xdata[0].date()) \
				+ ' - ' + str((xdata[len(xdata)-1]).date()) + ' UTC')

	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

	plt.legend()
	plt.ylabel('Temperature C')
	plt.grid(True)

	plt.tight_layout()

	plt.savefig(output_file, dpi=120)

	print 'Graph saved as ' + output_file

	plt.gcf().clear()

sqlite_conn = sqlite3.connect(config.SQLITE_DB_FILE, detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

cur = sqlite_conn.cursor()


print 'Selecting data from db'

cur.execute("SELECT time as '[timestamp]', temp from cpusensor WHERE time >= date('now','-1 day')")

plot_cpu_temperature(cur.fetchall(), output_file=config.PLOT_CPU_TEMPERATURE_DAY)

sqlite_conn.close()

print 'Done\n'

