# This program is written in Python3

from os import path
from csv import writer

def open_csv_first(logfile):
	# open csv file to record data
	if not path.exists(logfile, ):
		f = open(logfile, "a")
		writer = csv.writer(f)
		writer.writerow(["Time", "Value", "Over Threshold"])
		f.close()
