# This program is written in Python3
# Author : Masazumi Katoh
# coding : UTF-8
# Last Update : 2017/11/27

# to use MCP3008
from goipzero import MCP3008
# to check whether path exists or not
from os import path
# to get date and time
from datetime import datetime
from datetime import timedelta
# to write data to csv file
from csv import writer
# to run function per fixed time
import signal

# initial setting
# sampling rate [Hz]
sampling_rate = 10
# sampling period [sec]
sampling_period = timedelta(seconds = 1. / sampling_rate)
# save period [sec]
save_perio
