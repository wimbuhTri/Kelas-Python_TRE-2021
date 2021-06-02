import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib import cm

def read_using_csv():
	"""baca txt via csv library"""
	grid = np.empty(25)
	with open('sensor_read.txt') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		index = 0
		for row in csv_reader:
			buff = np.array(row,dtype="int")
			grid[index] = np.std(buff)
			index += 1
	return grid.reshape([5,5])

def read_using_numpy():
	"""baca txt via numpy library"""
	product = np.empty(25)
	grid = np.genfromtxt('sensor_read.txt',delimiter=',')
	index = 0
	for y in grid:
		product[index] = np.std(y)
		index += 1
	return product.reshape([5,5])

z = read_using_csv()
X = np.arange(5)
Y = np.arange(5)
X, Y = np.meshgrid(X, Y)
plt.figure(figsize = [8,5.5])
ax = plt.axes(projection="3d")
xax.plot_surface(X,Y,z, cmap=cm.coolwarm)
ax.set_title('Anomali pada Grid')
ax.set(xlabel='sumbu-x', ylabel='sumbu-y', zlabel='standar deviasi')
plt.show()