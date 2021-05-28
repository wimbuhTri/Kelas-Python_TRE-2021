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
	print("buka file complite_bar-plot.py")