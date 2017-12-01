# This program is written in Python3

from gpiozero import MCP3008
from datetime import datetime

def get_sensor_value(channel, value_list, length):
	t1 = datetime.now()
	input_value = MCP3008(channel = channel)
	t2 = datetime.now()
	present_value = V0 * input_value.value
	t3 = datetime.now()

	for i in range(length - 1):
		value_list[i] = value_list[i+1]

	t4 = datetime.now()
	value_list[length - 1] = present_value
	t5 = datetime.now()

	print("input :", t2 - t1)
	print("voltage :", t3 - t2)
	print("for loop :", t4 - t3)
	print("present :", t5 - t4)

	return value_list

get_sensor_value(0, [0,0,0,0,0,0], 6)
