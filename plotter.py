import matplotlib.pyplot as plt

def plot_weighted_data(clusters):
    # Split clusters into x, y and weights (charges)
    x = [point[0] for point in clusters]
    y = [point[1] for point in clusters]
    weights = [point[2] for point in clusters]

    # Normalize weights for better visualization. 
    # You can adjust this modification factor as needed. 100 is default
    modified_weights = [w/max(weights) * 100 for w in weights]
    #try total charge in cluster as well

    plt.scatter(x, y, s=modified_weights, alpha=0.6)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Weighted Data Points')
    plt.colorbar(label='Charge')
    plt.show()

# Example usage:
# plot_weighted_data(clusters)
