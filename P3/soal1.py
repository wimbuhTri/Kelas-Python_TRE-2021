bil1 = int(input("masukan angka pertama :"))
bil2 = int(input("masukan angka kedua :"))

jumlah = bil1+bil2
kurang = bil1-bil2
kali = bil1*bil2
bagi = bil1/bil2
modulus = bil1%bil2

print("hasil dari %d+%d = %d" %(bil1,bil2,jumlah))
print("hasil dari %d-%d = %d" %(bil1,bil2,kurang))
print("hasil dari %d*%d = %d" %(bil1,bil2,kali))
print("hasil dari %d/%d = %d" %(bil1,bil2,bagi))
print("hasil dari %d mod %d = %d" %(bil1,bil2,modulus))

#atau cara paling gampang tanpa peduli tipe data variabel sisipan
print("\n"*3)
print(f"hasil dari {bil1}+{bil2} = {jumlah}")
print(f"hasil dari {bil1}-{bil2} = {jumlah}")
print(f"hasil dari {bil1}*{bil2} = {jumlah}")
print(f"hasil dari {bil1}/{bil2} = {jumlah}")
print(f"hasil dari {bil1} mod {bil2} = {jumlah}")