# This program is written in Python3

from goipzero import MCP3008

def get_sensor_value(channel):
	input_value = MCP3008(channel = channel)
	present_value = input_value.value

	return present_value
