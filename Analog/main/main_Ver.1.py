# This program is written in Python3
# Author : Masazumi Katoh
# coding : UTF-8
# Last Update : 2017/12/1

# to use MCP3008
from gpiozero import MCP3008
# to check whether path exists or not
from os import path
# to get date and time
from datetime import datetime
from datetime import timedelta
# to sleep
from time import sleep
# to write data to csv file
import csv
# to run function per fixed time
import signal

# initial setting
# sampling rate [Hz]
# maximum rate is 60[Hz] @ Raspberry Pi 3
sampling_rate = 10
# sampling period [sec]
sampling_period = timedelta(seconds = 1. / sampling_rate)
# length of value list
length = 6
# list to save sensor values
value_list = [0 for i in range(length)]
# threshold value[V]
threshold = 1.
# flag to save judge_threshold
threshold_flag = False

# date
date = datetime.now().strftime("%Y%m%d")
# logfile's name
logfile = date + "_log.csv"

# channel to use MCP3008
channel = 0
# voltage range [V]
V0 = 3.3

def get_sensor_value(channel, value_list, length):
	input_value = MCP3008(channel = channel)
	present_value = V0 * input_value.value

	for i in range(length - 1):
		value_list[i] = value_list[i+1]

	value_list[length - 1] = present_value

	return value_list

def smoothing(value_list, length):
	smoothed_value = sum(value_list) / length

	return smoothed_value

def judge_threshold(smoothed_value, threshold):
	if (smoothed_value >= threshold):
		threshold_flag = True
	else:
		threshold_flag = False

	return threshold_flag

def calc_timedelta(standard_time, sampling_period):
	# calculate timedelta
	current_time = datetime.now()
	dif = current_time - standard_time
	timedelta = (dif % sampling_period).total_seconds()

	return timedelta

def write_to_csv(logfile, smoothed_value, threshold_flag):
	# open csv file to record data
	if path.exists(logfile):
		f = open(logfile, "a")
		writer = csv.writer(f)
	else:
		f = open(logfile, "a")
		writer = csv.writer(f)
		writer.writerow(["Time", "Value", "Over Threshold"])

	record_time = datetime.now().strftime("%H:%M:%S.%f")
	writer.writerow([record_time, "%.3f" %(smoothed_value), threshold_flag])
	print(record_time, "%.3f" %(smoothed_value), threshold_flag)

	f.close()

# get standard time
standard_time = datetime.now()

while True:
	t1 = datetime.now()
	value_list = get_sensor_value(channel, value_list, length)
	t2 = datetime.now()
	smoothed_value = smoothing(value_list, length)
	t3 = datetime.now()
	threshold_flag = judge_threshold(smoothed_value, threshold)
	t4 = datetime.now()
	write_to_csv(logfile, smoothed_value, threshold_flag)
	t5 = datetime.now()
	wait_time = sampling_period.total_seconds() - calc_timedelta(standard_time, sampling_period)
	t6 = datetime.now()
	print("get_sensor_value : ", t2 - t1)
	print("smoothing : ", t3 - t2)
	print("judge_threshold : ", t4 - t3)
	print("write_to_csv : ", t5 - t4)
	print("wait_time : ", t6 - t5)
	print("total :",t6 - t1)
	sleep(wait_time)
