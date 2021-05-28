#LEGB resolving rule
global_var = "I\'m global"

def outter():
	outter_var = "I\'m outer var"
	def inner():
		inner_var = "I\'m inner var"
		print(f'memanggil inner_var dari inner function: {inner_var}')
		print(f'memanggil outter_var dari inner function: {outter_var}')
		print(f'memanggil global_var dari inner function: {global_var}')	

	inner()
	print(f'memanggil outter_var dari outter function: {outter_var}')
	print(f'memanggil inner_var dari outter function: {inner_var}')
	

def function():
	local_var = "I\'m local"
	print(f'memanggil local_var dari dalam sub-program-fungsi: {local_var}')


function()
print(f'memanggil local_var milik sub-program-fungsi dari sub-program-utama: {local_var}')
#code yg inden-nya lebih dalem bisa akses var yg lebih cetek
#udah paham kegunaan return belum?
#upload source code ke pastebin!