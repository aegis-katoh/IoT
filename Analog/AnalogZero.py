# This program is written in Python3

from gpiozero import MCP3008
from time import sleep

# Maximum input voltage = 3.3V
V0 = 3.3

while True:
	input0 = MCP3008(channel=0)
	input1 = MCP3008(channel=1)
	input2 = MCP3008(channel=2)
	input3 = MCP3008(channel=3)
	input4 = MCP3008(channel=4)
	input5 = MCP3008(channel=5)
	input6 = MCP3008(channel=6)
	input7 = MCP3008(channel=7)
	
	voltage0 = V0 * input0.value
	voltage1 = V0 * input1.value
	voltage2 = V0 * input2.value
	voltage3 = V0 * input3.value
	voltage4 = V0 * input4.value
	voltage5 = V0 * input5.value
	voltage6 = V0 * input6.value
	voltage7 = V0 * input7.value
	
	print("A0 :", voltage0)
	print("A1 :", voltage1)
	print("A2 :", voltage2)
	print("A3 :", voltage3)
	print("A4 :", voltage4)
	print("A5 :", voltage5)
	print("A6 :", voltage6)
	print("A7 :", voltage7)

	sleep(0.5)
