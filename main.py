from matplotlib import pyplot as plt
import numpy as np

plt.figure()
ax = plt.axes(projection="3d")

x = np.arange(-4,4,0.05)
y = np.arange(-4,4,0.05)
X,Y = np.meshgrid(x,y)
Z = np.cos(np.sqrt(X ** 2 + Y ** 2))

ax.plot_surface(X,Y,Z,alpha=0.5,cmap="winter")
ax.set_xlabel("X")
ax.set_xlim(-4,4)
ax.set_ylabel("Y")
ax.set_ylim(-4,4)
ax.set_zlabel("Z")

plt.show()
