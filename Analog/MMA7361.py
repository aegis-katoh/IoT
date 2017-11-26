# This program is written in Python3

from gpiozero import MCP3008
from time import sleep

# Maximum input voltage = 3.3V
V0 = 3.3

while True:
	input0 = MCP3008(channel=0)
	input1 = MCP3008(channel=1)
	input2 = MCP3008(channel=2)

	voltage0 = V0 * input0.value
	voltage1 = V0 * input1.value
	voltage2 = V0 * input2.value

	print("X :", voltage0)
	print("Y :", voltage1)
	print("Z :", voltage2)

	sleep(1)
