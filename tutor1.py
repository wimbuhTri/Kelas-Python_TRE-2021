from time import sleep
"""ngajarin nge comment code"""

"""
print("command 1")
print("command 2")
print("command 3")
print("command 4")
"""
"""
bil1 = int (input("masukkan angka pertama : "))
bil2= int (input("masukkan angka kedua : "))

jumlah = bil1 + bil2
kurang = bil1 - bil2 
kali = bil1 * bil2
bagi = bil1/bil2
modulus = bil1 % bil2

print " hasil dari  %d  +  %d =  %d " % (bil1,bil2,jumlah)
print (" hasil dari  %d  –  %d =  %d " ,bil1,bil2,kurang)
print (" hasil dari  %d  *  %d =  %d " ,bil1,bil2,kali)
print (" hasil dari  %d  /  %d =  %d " ,bil1,bil2,bagi)

print (" hasil dari  %d  mod  %d =  %d "%(bil1,bil2,modulus))
#print "  "
"""


masukan = int(input("masukan nilai detik: "))

#jadi hari
day = int(masukan/(24*60*60))
print(f'hari: {day}')1

#sisa jam
sec_left_after_day = masukan%(24*60*60)
calc_hour = int(sec_left_after_day/(60*60))
print(f'jam {calc_hour}')

#jadi menit
sec_left_after_hour = sec_left_after_day%(60*60*calc_hour)
calc_mint = int(sec_left_after_hour/60)
print(f'mint {calc_mint}')

#jadi detik
sec_left_after_minute = sec_left_after_hour%calc_mint
print(f'sec {sec_left_after_minute}')

sleep(10)