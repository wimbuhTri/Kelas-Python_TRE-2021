def check(name,nim,grade):
	if grade <= 55:
		result = "tidak lulus"
	elif 55 <= grade < 80 :
		result = "mengulang"
	else:
		result = "lulus"
	print(f'siswa bernama {name} dengan identitas {nim} is {result}')


students = (("sekar","xxx",30),("adi","yyy",80),("galuh","yyy",60))

for student in students:
	check(student[0],student[1],student[2])