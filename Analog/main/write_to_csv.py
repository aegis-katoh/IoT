# This program is written in Python3

from csv import writer
from datetime import datetime

def write_to_csv(logfile, smoothed_value, threshold_flag):
	# open csv file to record data
	f = open(logfile, "a")
	writer = writer(f)
	record_time = datetime.now().strftime("%X")
	writer.writerow([record_time, smoothed_value, threshold_flag])
	f.close()
