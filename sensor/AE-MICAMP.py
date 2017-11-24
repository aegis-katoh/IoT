# This program is written in Python3

from gpiozero import MCP3008
from datetime import datetime
import csv

f = open("test.csv", "a")
writer = csv.writer(f)

while True:
	mic = MCP3008(channel=0)
	voltage = 3.3*mic.value
	time = datetime.now().strftime("%X")
	print(time, voltage)
	writer.writerow([time, voltage])
	
