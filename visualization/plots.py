import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_heatmap_midsection(density_grid, concentration_grid, time_step):
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.title(f"Density at time {time_step}")
    plt.imshow(density_grid[:,:,density_grid.shape[0] // 2], cmap='inferno')
    plt.colorbar(label='Density')
    
    plt.subplot(1, 2, 2)
    plt.title(f"Concentration at time {time_step}")
    plt.imshow(concentration_grid[:,:,concentration_grid.shape[0] // 2], cmap='inferno')
    plt.colorbar(label='Concentration')

    plt.show()

def plot_3d(density_grid, concentration_grid, time_step):
    x = np.arange(density_grid.shape[0])
    y = np.arange(density_grid.shape[1])
    z = np.arange(density_grid.shape[2])
    
    X, Y, Z = np.meshgrid(x, y, z)
    
    fig = plt.figure(figsize=(12, 5))
    
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.set_title(f"Density at time {time_step}")
    ax1.scatter(X.flatten(), Y.flatten(), Z.flatten(), c=density_grid.flatten(), cmap='inferno', vmin=0, vmax=1)
    plt.colorbar(ax1.collections[0], ax=ax1, label='Density')
    
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_title(f"Concentration at time {time_step}")
    ax2.scatter(X.flatten(), Y.flatten(), Z.flatten(), c=concentration_grid.flatten(), cmap='inferno', vmin=0, vmax=0.5)
    plt.colorbar(ax2.collections[0], ax=ax2, label='Concentration')

    plt.show()
