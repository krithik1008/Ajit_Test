import random 
import struct 

f= open("main.results",'w')
k=0
n=10
x=0xffffffb0

while(k<n):
	f.write("m[")
	f.write(hex(x))
	f.write("]=0x0000000a\n")
	f.write("asi=0x0a\n")
	x+=4
	k+=1	
f.close()
