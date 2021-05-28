inputan1 = int(input("data ke-1: "))
inputan2 = int(input("data ke-2: "))
inputan3 = int(input("data ke-3: "))


if inputan1 > inputan2 and inputan1 > inputan3:
	print("terbesar adalah inputan1")
elif inputan2 > inputan1 and inputan2 > inputan3:
	print("terbesar adalah inputan2")
else:
	print("terbesar adalah inputan3")