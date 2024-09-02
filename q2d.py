import matplotlib.pyplot as plt

# Observations
points = [(1, 4), (1, 3), (0, 4), (5, 1), (6, 2), (4, 0)]

# Cluster labels obtained from K-means clustering
labels = [1, 1, 1, 2, 2, 2]  # 1 for Cluster 1, 2 for Cluster 2

# Centroids
centroids = [(0.67, 3.67), (5, 1)]  # Centroid 1 and Centroid 2

# Separate the points into x and y coordinates for plotting
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# Create a color map for clusters
colors = ['blue' if label == 1 else 'red' for label in labels]

# Plot the points with cluster colors
plt.figure(figsize=(8, 8))
plt.scatter(x_coords, y_coords, color=colors, label='Points')

# Plot centroids
centroid_x, centroid_y = zip(*centroids)
plt.scatter(centroid_x, centroid_y, color=['lightblue', 'pink'], marker='x', s=100, label='Centroids')

# Annotate each point with its coordinates
for (x, y, label) in zip(x_coords, y_coords, labels):
    plt.text(x, y, f'({x},{y})', fontsize=12, ha='right', va='bottom')

# Annotate each centroid with its coordinates
for (x, y) in centroids:
    plt.text(x, y, f'({x},{y})', fontsize=12, ha='right', va='top', fontweight='bold', color='black')

# Set plot labels and title
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Plot of Observations for K-means Clustering (K=2)')
plt.grid(True)
plt.xticks(range(-1, 8))
plt.yticks(range(-1, 6))
plt.xlim(-1, 7)
plt.ylim(-1, 5)
plt.legend()

# Display the plot
plt.show()
