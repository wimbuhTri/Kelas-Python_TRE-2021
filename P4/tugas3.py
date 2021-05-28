X=int(input("1: "))
Y=int(input("2: "))
P=X+Y

if P >= 0:
	print("+")
	Q = X*Y
else:
	print("-")
	Q = X/Y

print(Q)