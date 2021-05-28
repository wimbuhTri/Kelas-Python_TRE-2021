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
	fig, ax = plt.subplots()
	x = np.arange(50)
	y = np.arange(50)
	plt.bar(y,x)
	plt.show()

	
