#!/usr/bin/python

import numpy as np

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import subprocess
import sys
import os

import config

def execute_system_cmd(cmd):
	return subprocess.check_output(cmd).decode('utf-8')

def get_sys_uptime():
	try:
		f = open( "/proc/uptime" )
		contents = f.read().split()
		f.close()
	except:
		return "Cannot open uptime file: /proc/uptime"
 
	total_seconds = float(contents[0])
 
	# Helper vars:
	MINUTE  = 60
	HOUR    = MINUTE * 60
	DAY     = HOUR * 24
 
	# Get the days, hours, etc:
	days    = int( total_seconds / DAY )
	hours   = int( ( total_seconds % DAY ) / HOUR )
	minutes = int( ( total_seconds % HOUR ) / MINUTE )
	seconds = int( total_seconds % MINUTE )
 
	# Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
	string = ""

	if days > 0:
		string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
	if len(string) > 0 or hours > 0:
		string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
	if len(string) > 0 or minutes > 0:
		string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
		string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
 
	return string;

def os_report():
	board_name = ''
	os_release = ''
	kernel_version = ''
	system_uptime = ''

	with open(config.BOARD_MODEL_FILE, 'r') as model_file:
		board_name = model_file.read()

	with open(config.OS_RELEASE_FILE, 'r') as os_release_file:
		os_release = os_release_file.readline().split('=')[1]
		os_release = os_release[1:-2]

	kernel_version = execute_system_cmd(['uname', '-r']).strip()

	system_uptime = get_sys_uptime()

	return board_name, os_release, kernel_version, system_uptime

def clock_and_voltages_report():
	cpu_freq = 'N/A'
	sys_mem = 'N/A'
	core_volt = 'N/A'
	sdram_volt = 'N/A'

	for line in execute_system_cmd(['vcgencmd', 'get_config', 'int']).strip().split('\n'):
		if 'arm_freq' in line:
			cpu_freq = line.split('=')[1]
			break

	for line in execute_system_cmd(['vcgencmd', 'get_mem', 'arm']).strip().split('\n'):
		if 'arm' in line:
			sys_mem = line.split('=')[1]
			break

	for line in execute_system_cmd(['vcgencmd', 'measure_volts', 'core']).strip().split('\n'):
		if 'volt' in line:
			core_volt = line.split('=')[1]

	for line in execute_system_cmd(['vcgencmd', 'measure_volts', 'sdram_c']).strip().split('\n'):
		if 'volt' in line:
			sdram_volt = line.split('=')[1]

	return cpu_freq, sys_mem, core_volt, sdram_volt

def plot_disks_usage(output_file):
	df_full = execute_system_cmd(['df']).strip().split('\n')

	print '\nPlotting disks usage pies'

	root_metric = []
	storage_metric = []

	for line in df_full:
		if 'root' in line:
			root_metric = line.split()

		if 'STORAGE' in line:
			storage_metric = line.split()

	labels = ['Free', 'Used']
	colors = ['yellowgreen', 'Red']

	fig, (ax1, ax2) = plt.subplots(1, 2)

	sizes = [int(root_metric[3]), int(root_metric[2])]

	ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
	ax1.axis('equal')
	ax1.set_title("Root")

	red_patch = mpatches.Patch(color='red', label='Used: ' + str(int(root_metric[2]) / 1024) + ' Mbytes')
	green_patch = mpatches.Patch(color='yellowgreen', label='Free: ' + str(int(root_metric[3]) / 1024) + ' Mbytes')
#	ax1.legend(handles=[red_patch, green_patch])

	sizes = [int(storage_metric[3]), int(storage_metric[2])]

	ax2.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
	ax2.axis('equal')
	ax2.set_title("Storage")

	red_patch = mpatches.Patch(color='red', label='Used: ' + str(int(storage_metric[2]) / 1024) + ' Mbytes')
	green_patch = mpatches.Patch(color='yellowgreen', label='Free: ' + str(int(storage_metric[3]) / 1024) + ' Mbytes')
#	ax2.legend(handles=[red_patch, green_patch])

	fig.tight_layout(pad=2)

	plt.savefig(output_file, dpi=120)

	print 'Pies saved as ' + output_file

def build_page(template_html_file, report_html_file):
	html_template = open(template_html_file).read()

	print 'Building web page using template ' + template_html_file

	os_report_list = os_report()
	clock_voltages_report = clock_and_voltages_report()

	print 'OS report:'
	print os_report_list

	print '\nClock and voltages report:'
	print clock_voltages_report

	board_name = os_report_list[0]
	os_release = os_report_list[1]
	kernel_version = os_report_list[2]
	system_uptime = os_report_list[3]

	cpu_freq = str(clock_voltages_report[0]) + ' MHz'
	sys_mem = clock_voltages_report[1]
	core_volt = clock_voltages_report[2]
	sdram_volt = clock_voltages_report[3]

	html_report_page = html_template.format(**locals())

	output_html = open(report_html_file, "w")
	output_html.write(html_report_page)
	output_html.close()

	print 'Report html page saved as ' + report_html_file

build_page(template_html_file=config.SYSTEM_HTML_TEMPLATE, report_html_file=config.SYSTEM_HTML_RESULT)
plot_disks_usage(output_file=config.PLOT_DISKS_USAGE)

print 'Done\n'

