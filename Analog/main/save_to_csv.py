# This program is written in Python3

from datetime import datetime
from csv import writer

def save_to_csv(value, flag):
	record_time = datetime.now().strftime("%X")

	writer.writerow([record_time, count, product_rate])
