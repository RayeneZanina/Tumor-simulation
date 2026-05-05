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

def sigmoid(grid, threshold):
    return 1 / (1 + np.exp(-15 * (grid - threshold)))

def plot_3d(density_grid, concentration_grid, time_step):
    x = np.arange(density_grid.shape[0])
    y = np.arange(density_grid.shape[1])
    z = np.arange(density_grid.shape[2])
    
    X, Y, Z = np.meshgrid(x, y, z)
    
    fig = plt.figure(figsize=(16, 5))
    
    alpha1 = sigmoid(density_grid.flatten(), 0.5) 
    colors1 = plt.cm.inferno(density_grid.flatten())
    colors1[:, -1] = alpha1
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.set_title(f"Density at time {time_step}")
    ax1.scatter(X.flatten(), Y.flatten(), Z.flatten(), c=colors1, cmap='inferno', vmin=0, vmax=1)
    ax1.set_xlabel('X-axis')
    ax1.set_ylabel('Y-axis')
    ax1.set_zlabel('Z-axis')
    plt.colorbar(ax1.collections[0], ax=ax1, label='Density')
    

    sm = plt.cm.ScalarMappable(cmap='inferno', norm=plt.Normalize(vmin=0, vmax=concentration_grid.max()))
    sm.set_array([])
    alpha2 = sigmoid(concentration_grid.flatten()/concentration_grid.max(), 0.5)
    colors2 = plt.cm.inferno(concentration_grid.flatten())
    colors2[:, -1] = alpha2
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_title(f"Concentration at time {time_step}")
    ax2.scatter(X.flatten(), Y.flatten(), Z.flatten(), c=colors2, cmap='inferno', vmin=0, vmax=concentration_grid.max())
    ax2.set_xlabel('X-axis')
    ax2.set_ylabel('Y-axis')
    ax2.set_zlabel('Z-axis')
    plt.colorbar(sm, ax=ax2, label='Concentration')

    plt.show()
