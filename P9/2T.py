"""
a.	Jumlah Pengendara tidak tentu
b.	Data kelengkapan Pengendara diinputkan
c.	Kelengkapan Pengendara yang diperiksa SIM dan STNK
d.	Denda : i. Tidak membawa SIM                     = Rp. 75.000
             ii. Tidak membawa STNK                 = Rp. 50.000
             iii. Tidak membawa SIM dan STNK = Rp. 125.000
e.	Dalam program yang anda buat ada satu sub program fungsi selain sub.program utama.
"""
print("Auto tilang\n[type E to exit]")
print("Menu:\n1.Tidak membawa SIM\n2.Tidak membawa STNK",("\n")*5)
index = 1

def HitungDenda(opsi):
	denda = 0
	if opsi.find("1") != -1:
		denda += 75000	
	if opsi.find("2") != -1:
		denda += 50000	
	if opsi.lower().find("e") != -1:
		quit()
	if opsi.find("1") and opsi.find("2") == -1:
		print("Ngetik yg bener!")
	print(denda)

while True:
	HitungDenda(input(f'{index} :: masukan opsi: '))
	index += 1