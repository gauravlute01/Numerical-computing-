import math
import numpy as np
import matplotlib.pyplot as plt

# Parameter
N = 1000
h = 0.01
theta0 = 1
omega0 = 1

# given function
def f_theta(theta, omega, l=1):
    return omega
def f_omega(theta , omega, g = 9.81, l =1):
    return -(g/l) * math.sin(theta)

# Rk4 method
def rk4_method(theta0, omega0, h, N):
    theta = [0]*N
    omega = [0]*N
    theta[0] = theta0
    omega[0] = omega0
    for i in range(1, N):
        k1_theta = h*f_theta(theta[i-1], omega[i-1])
        k1_omega = h*f_omega(theta[i-1], omega[i-1])

        k2_theta = h*f_theta(theta[i-1]+0.5*k1_theta, omega[i-1]+0.5*k1_omega)
        k2_omega = h*f_omega(theta[i-1]+0.5*k1_theta, omega[i-1]+0.5*k1_omega)

        k3_theta = h*f_theta(theta[i-1]+0.5*k2_theta, omega[i-1]+0.5*k2_omega)
        k3_omega = h*f_omega(theta[i-1]+0.5*k2_theta, omega[i-1]+0.5*k2_omega)

        k4_theta = h*f_theta(theta[i-1] + k3_theta, omega[i-1] + k3_omega)
        k4_omega = h*f_omega(theta[i-1] + k3_theta, omega[i-1] + k3_omega)

        theta[i] = theta[i-1] + (k1_theta + 2 * k2_theta + 2*k3_theta + k4_theta)/6
        omega[i] = omega[i-1] + (k1_omega + 2 * k2_omega + 2*k3_omega + k4_omega)/6
    return theta, omega

theta_rk4, omega_rk4 = rk4_method(theta0, omega0, h, N)
time = np.linspace(0, N*h, N)
plt.plot(time, theta_rk4, label = 'Theta (RK4)')
plt.plot(time, omega_rk4, label ='Omega (Rk4)')

plt.show()


