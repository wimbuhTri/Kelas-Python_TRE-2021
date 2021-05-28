from time import time
from random import randint


start = time()
for n in range(1000000):
	def decition(nilai):
		if nilai < 45:
			return f'nilai:{nilai} hasil: tidak lulus'
		elif 70 > nilai >= 45:
			return f'nilai:{nilai} hasil: mengulang'
		else :
			return f'nilai:{nilai} hasil: lulus'
	buff = f'{n} NIM: {randint(13223,14000)} {decition(randint(30,100))}'


print("\n\n\nruntime: ",time()-start)