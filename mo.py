#!/usr/bin/python3
from tool import *
print("hi")
def namedog(num):
	a="ALL"+"%04d"%(num)
	#print(a)
	b="F"+"%04d"%(num)+'CH1'
	c="F"+"%04d"%(num)+'CH2'
	d=[a,b,c]
	return d
	pass
for i in range(0,30):
	a=namedog(i)
	newdog=Autodog(a)
	newdog.readdog()
	print(newdog.fengdog())
	newdog.pindog()
	newdog.figdog()
	newdog.wridog()
