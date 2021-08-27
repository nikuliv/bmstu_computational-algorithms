from cogs import gauss, simpson, generate_function, integrate
import numpy as np
import matplotlib.pyplot as plt


def print_result(coeffs):
    phi_func = gauss
    theta_func = simpson

    x_values = list()
    y_values = list()
    for t in np.arange(0.05, 10, 0.05):
        func = generate_function(t)
        x_values.append(t)
        y_values.append(integrate(func, phi_func, theta_func, (0, np.pi/2), (0, np.pi/2), coeffs[0], coeffs[1]))

    plt.grid(True)
    plt.plot(x_values, y_values, "g")
    plt.xlabel("Tau", size=15)
    plt.ylabel("Значение интеграла", size=15)
    plt.show()
