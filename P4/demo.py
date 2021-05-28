watch_dog = 13
#float_variable = 5.0
nama_hari = "senin"

#f string
print(f"isi dari watch_dog adalah {watch_dog}")
print(f"isi dari nama_hari adalah {nama_hari}")

#old formating
print("isi dari watch_dog adalah %d" %watch_dog)
print("isi dari nama_hari adalah %s" %nama_hari)

#artimatik modulo
print(watch_dog/3)
print(int(watch_dog/3))
print(watch_dog%3)

#setiap jam genap pada hari selain selasa alarm berbunyi sekali
if watch_dog % 2 == 0 and nama_hari != "selasa":
	print("BEEPPP!!!")
#jika jam ganjil pada hari senin alarem bergetar
elif watch_dog % 2 == 1 and nama_hari == "senin":
	print("BZZZZT!!!")
else:
	print("seleksi kondisi tidak terpenuhi")