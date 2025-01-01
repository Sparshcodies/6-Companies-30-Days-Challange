import matplotlib.pyplot as plt

# Circle parameters
radius = 1415
xCenter = 807
yCenter = -784

# Rectangle parameters
x1, y1 = -733, 623
x2, y2 = -533, 1005

# Create a figure
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the rectangle
rectangle = plt.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=2, edgecolor='blue', facecolor='none', label='Rectangle')
ax.add_patch(rectangle)

# Plot the circle
circle = plt.Circle((xCenter, yCenter), radius, color='red', alpha=0.3, label='Circle')
ax.add_patch(circle)

# Set limits to visualize properly
ax.set_xlim(min(x1, xCenter - radius) - 200, max(x2, xCenter + radius) + 200)
ax.set_ylim(min(y1, yCenter - radius) - 200, max(y2, yCenter + radius) + 200)

# Add labels and legend
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Visualization of Circle and Rectangle Overlap')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()
