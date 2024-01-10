import matplotlib.pyplot as plt
import numpy as np

def plot_weighted_data(clusters, i):
    # Split clusters into x, y and weights (charges)
    x = [point[0] for point in clusters]
    y = [point[1] for point in clusters]
    weights = [point[2] for point in clusters]

    # Normalize weights for better visualization. 
    # You can adjust this modification factor as needed. 100 is default
    modified_weights = [w/max(weights) * 1000 for w in weights]
    #try total charge in cluster as well

    plt.scatter(x, y, s=modified_weights, alpha=0.6)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Weighted Data Points for cluster ' + str(i))
    #plt.errorbar(x, y, yerr=y_errors, fmt='o', markersize=5, alpha=0.6, ecolor='red', capsize=3)
    #plt.colorbar(label='Charge')
    plt.show()


def line(x, a, b):
    return a * x + b

def plot_weighted_data_with_fit(clusters, i, m):
    # Split clusters into x, y and weights (charges)
    x = [point[0] for point in clusters]
    y = [point[1] for point in clusters]
    weights = [point[2] for point in clusters]
    xs = []
    for x, _, _, in clusters:
        xs = xs.append(x)
    x_fit = np.linspace(xs[0], xs[-1], 100)
    y_fit = line(x_fit, m.values['a'], m.values['b'])
    #return x_fit, y_fit

    # Normalize weights for better visualization. 
    # You can adjust this modification factor as needed. 100 is default
    modified_weights = [w/max(weights) * 1000 for w in weights]
    #try total charge in cluster as well

    plt.scatter(x, y, s=modified_weights, alpha=0.6)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Weighted Data Points for cluster ' + str(i))
    plt.plot(x_fit, y_fit, 'r-', label=f'Fit: y = ({m.values["a"]:.2f}x + {m.values["b"]:.2f})')
    #plt.errorbar(x, y, yerr=y_errors, fmt='o', markersize=5, alpha=0.6, ecolor='red', capsize=3)
    #plt.colorbar(label='Charge')
    plt.show()

def plot_histogram(beta_values, title, x_axis):

    # Extracting the differences between beta_true and beta_calculated
    #differences = [true - calculated for calculated, true in beta_values]

    # Plotting the histogram
    plt.hist(beta_values, bins=30, facecolor='blue', edgecolor='black', alpha=0.7)
    plt.xlabel(x_axis)
    plt.ylabel('Frequency')
    plt.title(title)
    plt.grid(True)
    plt.show()

def normal_plot(data_list, title, x_axis, y_axis):

    x, y = zip(*data_list)

    # Create the plot
    plt.scatter(x, y)

    # Set the title and labels for the axes
    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

    # Show the plot
    plt.show()

def calculate_line_points(x_center, y_center, true_beta, length=10):

    true_beta_rad = np.deg2rad(true_beta)

    dx = length * np.cos(true_beta_rad)
    dy = length * np.sin(true_beta_rad)

    point1 = (x_center - dx, y_center - dy)
    point2 = (x_center + dx, y_center + dy)

    return point1, point2

#add pixel plot somewhere here