import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 1.0         # Total time (x-axis range)
n_steps = 100   # Number of steps per path
n_paths = 15    # Number of different lines (realizations)
dt = T / n_steps

# 1. Setup Time
t = np.linspace(0, T, n_steps + 1)

# 2. Generate Random Steps
# Brownian motion increments dW are normally distributed with mean 0 and variance dt
# scale (std dev) = sqrt(dt)
increments = np.random.normal(0, np.sqrt(dt), size=(n_paths, n_steps))

# 3. Calculate Paths (Cumulative Sum)
# We calculate the cumulative sum of steps to get the path positions
paths = np.cumsum(increments, axis=1)

# Add the starting point (0) to the beginning of every path
paths = np.hstack((np.zeros((n_paths, 1)), paths))

# 4. Plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Match the gray visual style
bg_color = '#d9d9d9' # Light gray background
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

# Plot each line
for i in range(n_paths):
    ax.plot(t, paths[i], linewidth=1.5, alpha=0.8)

# Labels and Title
ax.set_title("Brownian Motion", fontsize=16)
ax.set_xlabel("$t$", fontsize=14)    # Time
ax.set_ylabel("$X(t)$", fontsize=14) # Displacement

# Grid
ax.grid(True, color='gray', alpha=0.3)
ax.set_xlim(0, T)

plt.show()