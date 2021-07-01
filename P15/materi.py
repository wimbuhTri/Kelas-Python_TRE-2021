def perhitungan(parameter1,parameter2):
	"""Menghitung jumlah dan selisih dua parameter yang disediakan"""
	hasil_penjumlahan = parameter1 + parameter2
	selisih = abs(parameter1 - parameter2)
	return hasil_penjumlahan, selisih

hasil_oprasi_tambah, hasil_oprasi_selisih  = perhitungan(10,20)
hanya_butuh_hasil_tambah, _ = perhitungan(40,50)