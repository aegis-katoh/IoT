# This program is written in Python3

from gpiozero import MCP3008

# Maximum input voltage = 3.3V
V0 = 3.3

input0 = MCP3008(channel=0)
input1 = MCP3008(channel=1)

voltage0 = V0 * input0.value
voltage1 = V0 * input1.value
