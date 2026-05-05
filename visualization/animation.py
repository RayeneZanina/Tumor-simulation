import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_heatmap_section(density_grids, concentration_grids, time_steps):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    im1 = axes[0].imshow(density_grids[0][:,:,density_grids[0].shape[2] // 2], cmap='inferno')
    axes[0].set_title(f"Density at time 0")
    plt.colorbar(im1, ax=axes[0], label='Density')
    im2 = axes[1].imshow(concentration_grids[0][:,:,concentration_grids[0].shape[2] // 2], cmap='inferno')
    axes[1].set_title(f"Concentration at time 0")
    plt.colorbar(im2, ax=axes[1], label='Concentration')

    def update(frame):
        axes[0].clear()
        axes[1].clear()
        
        axes[0].set_title(f"Density at time {frame}")
        axes[0].imshow(density_grids[frame][:,:,density_grids[frame].shape[2] // 2], cmap='inferno')
        
        axes[1].set_title(f"Concentration at time {frame}")
        axes[1].imshow(concentration_grids[frame][:,:,concentration_grids[frame].shape[2] // 2], cmap='inferno')
    
    ani = animation.FuncAnimation(fig, update, frames=time_steps, repeat=False, interval=50)
    plt.show()