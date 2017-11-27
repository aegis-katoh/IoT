# This program is written in Python3

from goipzero import MCP3008

def get_sensor_value(A_PIN):
	input_value = MCP3008(channel = A_PIN)
	value = input_value.value

	return value
