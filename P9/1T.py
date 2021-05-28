"""
a.	Jumlah mahasiswa 25 org
b.	Nama mahasiswa, NIM dan nilai praktikum diinputkan
c.	Lulus  : nilai > = 70 ; Mengulang  : 70 > nilai >= 45; Tidak Lulus : nilai < 45
d.	Data nama, NIM, nilai praktikum dan keterangan Kelulusan mahasiswa ditampilkan
e.	Dalam program yang anda buat ada satu sub program fungsi selain sub.program utama. 
   Catatan : -  pergunakan Perulangan Proses for dan Pengujian Kondisi menggunakan if .. elif  
                        ..   else  !
-	tampilkan listing program dan hasil eksekusi serta analisislah program anda 
"""
from random import randint
names = ["Khaznan Octaviana","Dee Rahmasari","Syarief Arahman","Dede Bisri","Achmad Abrianto","Jeremiah Adriarso","Mario Alghifari","Reynaldi Pasha","Farizi Djiddy","Fariz Ulfania","Revi Andrawida","Aldi Virani","Dimas Aisyah","Fahlian S","Yusuf arhorasan","Syahrul Avicenna Jaya","Akbar Sastrawan","Ferdiansyah Primanelza","Herdaru Lukman Eda","Faishal Shalimah"]



def decition(nilai):
	if nilai < 45:
		return f'nilai:{nilai} hasil: tidak lulus'
	elif 70 > nilai >= 45:
		return f'nilai:{nilai} hasil: mengulang'
	else :
		return f'nilai:{nilai} hasil: lulus'

for name in names:
	print(f'{name} NIM: {randint(13223,14000)} {decition(randint(30,100))}')