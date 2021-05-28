tahun = 2004

if tahun in range(0,3000):
	print("true")
else:
	print("false")

if (tahun % 4 == 0):	
	if tahun % 100 == 0:
		if tahun % 400 == 0 :
			print("tahun kabisat")
		else:
			print("bukan tahun kabisat")
	else:		
		print("bukan tahun kabisat")
else:
	print("bukan tahun kabisat")