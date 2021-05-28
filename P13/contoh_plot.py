import numpy as np
import matplotlib.pyplot as plt

def lineplot():
	x = np.linspace(0,2*np.pi,100)
	cos_x = np.cos(x)
	plt.plot(cos_x)	
	plt.show()

def scatter():
	x = np.linspace(0,np.pi,50)
	cos_x = np.cos(x)
	plt.scatter(x,cos_x)
	plt.show()

def bar():	
	x = np.arange(5)
	"""
	y = np.linspace(0,3,5)
	labels = ["toddler","childhood","teens","mature","old"]
	fig, ax = plt.subplots()
	ax.bar(y,x)
	ax.set_ylabel('Potential')
	ax.set_xlabel('Stages')
	ax.set_title('Linear Gibberish Progession')
	#ax.set_xticks(x)
	ax.set_xticklabels(labels)
	#ax.legend()
	"""
	fig = plt.figure()
	ax = fig.add_axes([0,0,1,1])
	langs = ['C', 'C++', 'Java', 'Python', 'PHP']
	students = [23,17,35,29,12]
	ax.bar(langs,x)
	plt.show()

bar()