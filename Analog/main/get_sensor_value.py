# This program is written in Python3

from goipzero import MCP3008

def get_sensor_value(channel, value_list, length):
	input_value = MCP3008(channel = channel)
	present_value = input_value.value

	for i in range(lenght - 1):
		value_list[i] = value_list[i+1]

	value_list[length - 1] = present_value

	return value_list
