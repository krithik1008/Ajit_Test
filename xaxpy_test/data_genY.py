import random 
import struct 

f= open("datay.s",'w')
f.write('.section ".text" \n.align 4\n.global genyd \n.type genyd, #function\ngenyd:\n\tsave  %sp, -120, %sp\n\tset datay,%i0\n\trestore\n\tretl\n\tnop\n.section ".data"\n.align 8\n.global datay\ndatay:\n')

for i in range(0,3200):
	f.write(".word	")
	x=random.randrange(0, 500, 3)
	f.write(str(x))
	f.write('\n')
	

f.write('\n')

f.write('.section ".text" \n.align 4\n.global genyf \n.type genyf, #function\ngenyf:\n\tsave  %sp, -120, %sp\n\tset datayf,%i0\n\trestore\n\tretl\n\tnop\n.section ".data"\n.align 8\n.global datayf\ndatayf:\n')

for i in range(0,3200):
	f.write(".word	")
	x=random.uniform(-2.56,0)
	s = struct.pack('>f', x)
	i = struct.unpack('>I', s)[0]
	f.write(hex(i))
	f.write('\n')
	
	
f.close()
