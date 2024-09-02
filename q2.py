import matplotlib.pyplot as plt

# Observations
points = [(1, 4), (1, 3), (0, 4), (5, 1), (6, 2), (4, 0)]

# Separate the points into x and y coordinates for plotting
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# Plot the points
plt.figure(figsize=(6, 6))
plt.scatter(x_coords, y_coords, color='blue')

# Annotate each point with its coordinates
for (x, y) in points:
    plt.text(x, y, f'({x},{y})', fontsize=12, ha='right', va='bottom')

# Set plot labels and title
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Plot of Observations for K-means Clustering (K=2)')
plt.grid(True)
plt.xticks(range(-1, 8))
plt.yticks(range(-1, 6))
plt.xlim(-1, 7)
plt.ylim(-1, 5)

# Display the plot
plt.show()
