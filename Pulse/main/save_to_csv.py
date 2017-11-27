# This program is written in Python3

from os import path
import csv
from datetime import datetime

def save_to_csv(dum1, dum2):
	global logfile
	global count
	global save_period

	record_time = datetime.now().strftime("%X")
	product_rate = calc_product_rate(count, save_period)

	# open csv file to record data
	if path.exists(logfile, ):
		f = open(logfile, "a")
		writer = csv.writer(f)
	else:
		f = open(logfile, "a")
		writer = csv.writer(f)
		writer.writerow(["Time", "Count", "Rate"])

	# record data
	writer.writerow([record_time, count, product_rate])
	# close csv file
	f.close()

	count = reset_count()
