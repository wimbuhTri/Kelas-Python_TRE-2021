y = [10,20,30,40,50,60,70,80,90] 
for x in y:	
	if x == 50:
		print("skipping")
		continue 
	if x > 70: 
		print(f'break > {x}')
		break 		
	print(f'debug: {x}')
else: 
	print('Perulangan selesai')

"""saat x == 50 stetement di bawahnya tidak dilanjutkan dan langsung ke iterasi selanjutnya. looping selesai pada value x == 80"""