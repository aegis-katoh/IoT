# This program is written in Python3

from csv import writer
from datetime import datetime

def open_csv_first(logfile):
	# open csv file to record data
	if not path.exists(logfile, ):
		f = open(logfile, "a")
		writer = writer(f)
		writer.writerow(["Time", "Value", "Over Threshold"])
		f.close()
