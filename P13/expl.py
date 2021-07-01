import matplotlib.pyplot as plt
import numpy as np

#data = np.random.randint(20, 50, 25)
data = np.array([10000,1000,100,10,1])
#data = read_using_numpy()
grid_ID = np.arange(len(data))

fig, ax = plt.subplots()
ax.bar(grid_ID, data, width=0.8, align='center')
ax.set(xticks=range(grid_ID.size)) #label tick pada x axis
ax.set_ylabel('Potential')
ax.set_xlabel('Stages')
ax.set_title('Noise Progession')
plt.show()

"""starter code by Joe Kington Posted on stackOverflow 
https://stackoverflow.com/questions/27083051/matplotlib-xticks-not-lining-up-with-histogram"""