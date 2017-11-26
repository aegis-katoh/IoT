# This program is written in Python3

from gpiozero import MCP3008
from math import log
from time import sleep

B = 3380
R0 = 10000
R1 = 4700
V0 = 3.3
T0 = 25

def GetTemp(B, R0, R1, V0, T0):
	Vpre = MCP3008(channel = 0)
	V = V0*Vpre.value
	#print("V : ", V)
	R = (V0/V - 1)*R1
	#print("R : ", R)
	T=(1)/((1/B)*(log(R/R0)) +(1)/(T0+273)) - 273
	#print("1/B : ", (1/B), "log(R/R0)", log(R/R0))
	#print("temperature : ", T)
	return T

while True:
	T = GetTemp(B, R0, R1, V0, T0)
	print("temperature : ", T)
	sleep(1)
