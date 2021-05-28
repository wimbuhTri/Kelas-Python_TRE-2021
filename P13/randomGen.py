from random import randint

RECORD_LEN = 250

NIM = int(input("Masukan NIM: "))
#TarGrid = randint(0,NIM%25)
TarGrid = NIM%25
print(TarGrid)
buff = []
dic = {}
index = 0
for gridID in range(25):
	if gridID == TarGrid:		
		for m in range(RECORD_LEN):
			if m != 0:
				buff.append(",")
			buff.append(randint(28,57))
	else:
		for m in range(RECORD_LEN):
			if m != 0:
				buff.append(",")
			buff.append(randint(30,55))
	dic[index] = buff
	index += 1
	buff = []


f = open("sensor_read.txt", "w")
for key in dic:	
	for element in dic[key]:
		f.write(str(element))
	f.write("\n")
f.close()