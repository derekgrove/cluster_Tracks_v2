import math
import numpy as np
from iminuit import Minuit
import matplotlib.pyplot as plt

def line(x, a, b):
    return a * x + b

def x_line(y, c, d):
    return c * y + d


def iminuit_chi2(result_with_charge, x_or_y):
    # Extracting data from result_with_charge
    x = np.array([item[0] for item in result_with_charge])
    y = np.array([item[1] for item in result_with_charge])
    weights = np.array([item[2] for item in result_with_charge])
    errors = np.array([item[3] for item in result_with_charge])
    #y_errors[3] = y_errors[3]*.1
    #y_errors[0] = y_errors[0]*10
    #y_errors[6] = y_errors[6]*10
    print("errors:")
    print(errors)
    print("y:")
    print(y)
    
    if x_or_y == 'y':
    # Chi-squared function
        def chi2(a, b):
            y_model = line(x, a, b)
            chi = (y - y_model) ** 2 / errors**2
            return np.sum(chi)
    if x_or_y == 'x':
    # Chi-squared function
        def chi2(a, b):
            y_model = line(x, a, b)
            chi = (y - y_model) ** 2 / errors**2
            return np.sum(chi)
    '''if x_or_y == 'x':
        def chi2(c, d):
            x_model = x_line(x, c, d)
            chi = (x - x_model) ** 2 / errors**2
            return np.sum(chi)'''

    # Minimize chi-squared
    if x_or_y == 'y':
        m = Minuit(chi2, a=1, b=0)
        m.errordef = 1
        m.errors['a'] = 0.1
        m.errors['b'] = 0.1
        m.migrad()  # run the minimizer
        beta_angle = angle_from_slope(m.values['a'])
        return m, weights, x, y, errors, beta_angle
    '''if x_or_y == 'x':
            m = Minuit(chi2, c=1, d=0)
            m.errordef = 1
            m.errors['c'] = 0.1
            m.errors['d'] = 0.1
            m.migrad()  # run the minimizer
            beta_angle = angle_from_slope(m.values['c'])
            return m, weights, x, y, errors, beta_angle'''
    if x_or_y == 'x':
        m = Minuit(chi2, a=1, b=0)
        m.errordef = 1
        m.errors['a'] = 0.1
        m.errors['b'] = 0.1
        m.migrad()  # run the minimizer
        beta_angle = angle_from_slope(m.values['a'])
        return m, weights, x, y, errors, beta_angle
def plot_imin_obj_y(m, weights, x, y, errors, calc_beta, true_beta, i):
    # Plotting
    plt.scatter(x, y, c='blue', marker='o', label='Data points', s=weights*100)  # scaling down the point size for clarity
    x_fit = np.linspace(min(x), max(x), 400)
    y_fit = line(x_fit, m.values['a'], m.values['b'])
    dof = len(x) - 2  # degrees of freedom = number of data points - number of fitted parameters
    reduced_chi2 = m.fval / dof
    print('reduced chi square:', reduced_chi2)
    plt.xlim(min(x)-1, max(x)+1)
    plt.ylim(min(y)-1, max(y)+1)
    plt.plot(x_fit, y_fit, 'r-', label=f'Fit: y = ({m.values["a"]:.2f} +- {m.errors["a"]:.2f}) x + ({m.values["b"]:.2f}+- {m.errors["b"]:.2f})')
    plt.errorbar(x, y, yerr=errors, fmt='o', markersize=5, alpha=0.6, ecolor='blue', capsize=3)
    #print(y_errors)
    #print(1/(math.sqrt(12)))
    #point1, point2 = true_beta_line
    # Plot the true beta line
    #plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'g--', label='True Beta Line')

    
    beta_calc_text = f"Calc Beta Angle: {calc_beta:.2f}°"
    beta_true_text = f"True Beta Angle: {true_beta:.2f}°"
    #x_position = min(x) + 0.9 * (max(x) - min(x))  # 10% from the left edge
    #y_position = max(y) + 0.9 * (max(y) - min(y))  # 10% from the top edge
    plt.text(1, 0, beta_calc_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    plt.text(1, 0.1, beta_true_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    #print('chi square:', m.fval)
    print('errors in slope:', m.errors["a"])
    print('errors in y-intercept:', m.errors["b"])
    print('beta angle from iminuit: ', angle_from_slope(m.values['a']))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Weighted Linear Fit Cluster ' + str(i))
    plt.grid(True)
    plt.show()

def plot_imin_obj_x(m, weights, x, y, errors, calc_beta, true_beta, i):
    # Plotting
    plt.scatter(y, x, c='blue', marker='o', label='Data points', s=weights*100)  # scaling down the point size for clarity
    y_fit = np.linspace(min(x), max(x), 400)
    x_fit = line(y_fit, m.values['a'], m.values['b'])
    dof = len(x) - 2  # degrees of freedom = number of data points - number of fitted parameters
    reduced_chi2 = m.fval / dof
    print('reduced chi square:', reduced_chi2)
    plt.xlim(min(x)-1, max(x)+1)
    plt.ylim(min(y)-1, max(y)+1)
    plt.plot(y_fit, x_fit, 'r-', label=f'Fit: y = ({m.values["a"]:.2f} +- {m.errors["a"]:.2f}) x + ({m.values["b"]:.2f}+- {m.errors["b"]:.2f})')
    plt.errorbar(x, y, yerr=errors, fmt='o', markersize=5, alpha=0.6, ecolor='blue', capsize=3)
    #print(y_errors)
    #print(1/(math.sqrt(12)))
    #point1, point2 = true_beta_line
    # Plot the true beta line
    #plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'g--', label='True Beta Line')

    
    beta_calc_text = f"Calc Beta Angle: {calc_beta:.2f}°"
    beta_true_text = f"True Beta Angle: {true_beta:.2f}°"
    #x_position = min(x) + 0.9 * (max(x) - min(x))  # 10% from the left edge
    #y_position = max(y) + 0.9 * (max(y) - min(y))  # 10% from the top edge
    plt.text(1, 0, beta_calc_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    plt.text(1, 0.1, beta_true_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    #print('chi square:', m.fval)
    print('errors in slope:', m.errors["a"])
    print('errors in y-intercept:', m.errors["b"])
    print('beta angle from iminuit: ', angle_from_slope(m.values['a']))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Weighted Linear Fit Cluster ' + str(i))
    plt.grid(True)
    plt.show()

'''def plot_imin_obj_x(m, weights, x, y, errors, calc_beta, true_beta, i):
    # Plotting
    plt.scatter(x, y, c='blue', marker='o', label='Data points', s=weights*100)  # scaling down the point size for clarity
    x_fit = np.linspace(min(x), max(x), 400)
    y_fit = x_line(x_fit, m.values['c'], m.values['d'])
    dof = len(x) - 2  # degrees of freedom = number of data points - number of fitted parameters
    reduced_chi2 = m.fval / dof
    print('reduced chi square:', reduced_chi2)
    plt.xlim(min(x)-1, max(x)+1)
    plt.ylim(min(y)-1, max(y)+1)
    plt.plot(x_fit, y_fit, 'r-', label=f'Fit: y = ({m.values["a"]:.2f} +- {m.errors["a"]:.2f}) x + ({m.values["b"]:.2f}+- {m.errors["b"]:.2f})')
    plt.errorbar(x, y, xerr=errors, fmt='o', markersize=5, alpha=0.6, ecolor='red', capsize=3)
    #print(y_errors)
    #print(1/(math.sqrt(12)))
    
    beta_calc_text = f"Calc Beta Angle: {calc_beta:.2f}°"
    beta_true_text = f"True Beta Angle: {true_beta:.2f}°"
    #x_position = min(x) + 0.9 * (max(x) - min(x))  # 10% from the left edge
    #y_position = max(y) + 0.9 * (max(y) - min(y))  # 10% from the top edge
    plt.text(1, 0, beta_calc_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    plt.text(1, 0, beta_true_text, 
            fontsize=10, 
            transform=plt.gca().transAxes, 
            horizontalalignment='right', 
            verticalalignment='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, pad=5))
    #print('chi square:', m.fval)
    print('errors in slope:', m.errors["a"])
    print('errors in y-intercept:', m.errors["b"])
    print('beta angle from iminuit: ', angle_from_slope(m.values['a']))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Weighted Linear Fit Cluster ' + str(i))
    plt.grid(True)
    plt.show()'''


#include these functions to get beta angle (angle of major axis) from the calculated slope:
def angle_from_slope(m):
    angle_rad = math.atan(m)
    angle_deg = math.degrees(angle_rad)
    return angle_deg
