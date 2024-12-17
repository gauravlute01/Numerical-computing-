#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import matplotlib.pyplot as plt

alpha = 1.1
beta  = 0.4
gamma = 0.4
delta = 0.1


t = np.linspace(0, 25, 1000)
dt = t[1] - t[0]

# Initial condition for the prey population
x0 = 10


#initial value
initial_values = [(x0, y0) for y0 in [1, 2, 5, 7, 10, 12, 15]]


# RK4
def runge_kutta(f, X0, t, alpha, beta, delta, gamma):
    X = np.zeros((len(t), len(X0)))
    X[0] = X0
    
    for i in range(1, len(t)):
        k1 = f(X[i-1], t[i-1], alpha, beta, delta, gamma)
        k2 = f(X[i-1] + dt/2*k1, t[i-1] + dt/2, alpha, beta, delta, gamma)
        k3 = f(X[i-1] + dt/2*k2, t[i-1] + dt/2, alpha, beta, delta, gamma)
        k4 = f(X[i-1] + dt*k3, t[i-1] + dt, alpha, beta, delta, gamma)
        X[i] = X[i-1] + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
    return X

def lotka_volterra(X, t, alpha, beta, delta, gamma):
    x, y = X
    dxdt = (alpha*x - beta*x*y)
    dydt = (-gamma*y) + (delta*x*y)
    return np.array([dxdt, dydt])


plt.figure(figsize=(12, 8))
for initial_condition in initial_values:
    matrix = runge_kutta(lotka_volterra, initial_condition, t, alpha, beta, delta, gamma)
    #print(solution)
    x, y = matrix.T
    #print(x)
    plt.plot(x, y, label=f'y0 = {initial_condition[1]}')
    
plt.title('Phase-Space Plot of various initial condition')
plt.xlabel('Prey Population')
plt.ylabel('Predator Population')
plt.ylim(0, 16)
plt.legend()
plt.grid()
plt.show()


# In[18]:


import numpy as np
import matplotlib.pyplot as plt

# Define the Lotka-Volterra equations
def lotka_volterra(X, t, alpha, beta, delta, gamma):
    x, y = X
    dxdt = (alpha*x - beta*x*y)
    dydt = (-gamma*y) + (delta*x*y)
    return np.array([dxdt, dydt])

# Parameters for the model
alpha = 1.1   # Prey growth rate
beta = 0.4    # Predation rate
gamma = 0.4   # Predator death rate
delta = 0.1   # Predator reproduction rate

# Time points
t = np.linspace(0, 25, 1000)
dt = t[1] - t[0]

# Runge-Kutta 4th order method
def runge_kutta(f, X0, t, alpha, beta, delta, gamma):
    X = np.zeros((len(t), len(X0)))
    X[0] = X0
    for i in range(1, len(t)):
        k1 = f(X[i-1], t[i-1], alpha, beta, delta, gamma)
        k2 = f(X[i-1] + dt/2*k1, t[i-1] + dt/2, alpha, beta, delta, gamma)
        k3 = f(X[i-1] + dt/2*k2, t[i-1] + dt/2, alpha, beta, delta, gamma)
        k4 = f(X[i-1] + dt*k3, t[i-1] + dt, alpha, beta, delta, gamma)
        X[i] = X[i-1] + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
    return X

# Initial condition for the prey population
x0 = 10

# Different initial conditions for the predator population
initial_conditions = [(x0, y0) for y0 in [1, 2, 5, 7, 10, 12, 15]]

# Create a figure for the phase-space plots
plt.figure(figsize=(12, 8))

# Plot phase-space plots for different initial conditions
for initial_condition in initial_conditions:
    solution = runge_kutta(lotka_volterra, initial_condition, t, alpha, beta, delta, gamma)
    x, y = solution.T
    plt.plot(x, y, label=f'y0 = {initial_condition[1]}')

# Add titles and labels
plt.title('Phase-Space Plot of the Lotka-Volterra Model')
plt.xlabel('Prey Population')
plt.ylabel('Predator Population')
plt.ylim(0, 16)
plt.legend()
plt.grid()
plt.show()


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def lotka_volterra(z, t, alpha, beta, gamma, delta):
    x, y = z
    dxdt = (alpha*x - beta*x*y)
    dydt = (-gamma*y) + (delta*x*y)
    return [dxdt, dydt]

alpha = 1.1
beta = 0.4
gamma = 0.4
delta = 0.1

t = np.linspace(0, 200, 1000)
x0 = 10
y0_values = [1, 2, 5, 7, 10, 12, 15]
plt.figure(figsize=(10, 6))

for y0 in y0_values:
    z0 = [x0, y0]
    sol = odeint(lotka_volterra, z0, t, args=(alpha, beta, gamma, delta))
    plt.plot(sol[:, 0], sol[:, 1], label=f'y0: {y0}')
    
plt.legend()
plt.grid()
plt.show()


# In[6]:


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Lotka-Volterra equations
def lotka_volterra(z, t, alpha, beta, delta, gamma):
    x, y = z
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Parameters
alpha = 0.1  # Natural growth rate of prey
beta = 0.02  # Natural dying rate of prey due to predation
gamma = 0.3  # Natural dying rate of predators
delta = 0.01  # Factor describing how many prey are needed to produce a new predator

# Initial conditions: 40 prey and 9 predators
z0 = [40, 9]

# Time points
t = np.linspace(0, 200, 1000)

# Solve ODE
solution = odeint(lotka_volterra, z0, t, args=(alpha, beta, delta, gamma))
x, y = solution.T

# Plotting results
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='Prey population', color='b')
plt.plot(t, y, label='Predator population', color='r')
plt.xlabel('Time')
plt.ylabel('Population size')
plt.title('Lotka-Volterra Predator-Prey Model')
plt.legend()
plt.grid()
plt.show()


# In[9]:


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Lotka-Volterra equations
def lotka_volterra(z, t, alpha, beta, delta, gamma):
    x, y = z
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Parameters
alpha = 0.1  # Natural growth rate of prey
beta = 0.02  # Natural dying rate of prey due to predation
gamma = 0.3  # Natural dying rate of predators
delta = 0.01  # Factor describing how many prey are needed to produce a new predator

# Initial conditions: 40 prey and 9 predators
z0 = [40, 9]

# Time points
t = np.linspace(0, 200, 1000)

# Solve ODE
solution = odeint(lotka_volterra, z0, t, args=(alpha, beta, delta, gamma))
x, y = solution.T



# Phase diagram

plt.plot(x, y, color='purple')
plt.xlabel('Prey population')
plt.ylabel('Predator population')
plt.title('Phase Diagram')
plt.grid()

plt.tight_layout()
plt.show()


# In[10]:


import numpy as np
import matplotlib.pyplot as plt

def lotka_volterra(z, t, alpha, beta, gamma, delta):
    x, y = z
    dxdt = alpha * x - beta * x * y
    dydt = -gamma * y + delta * x * y
    return np.array([dxdt, dydt])

def runge_kutta_4(f, z0, t, args):
    n = len(t)
    z = np.zeros((n, len(z0)))
    z[0] = z0
    for i in range(1, n):
        h = t[i] - t[i - 1]
        k1 = f(z[i - 1], t[i - 1], *args)
        k2 = f(z[i - 1] + 0.5 * h * k1, t[i - 1] + 0.5 * h, *args)
        k3 = f(z[i - 1] + 0.5 * h * k2, t[i - 1] + 0.5 * h, *args)
        k4 = f(z[i - 1] + h * k3, t[i - 1] + h, *args)
        z[i] = z[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return z

alpha = 1.1
beta = 0.4
gamma = 0.4
delta = 0.1

t = np.linspace(0, 200, 1000)
x0 = 10
y0_values = [1, 2, 5, 7, 10, 12, 15]
plt.figure(figsize=(10, 6))

for y0 in y0_values:
    z0 = [x0, y0]
    sol = runge_kutta_4(lotka_volterra, z0, t, args=(alpha, beta, gamma, delta))
    plt.plot(sol[:, 0], sol[:, 1], label=f'y0: {y0}')
    
plt.xlabel('Prey Population')
plt.ylabel('Predator Population')
plt.title('Lotka-Volterra Model (Runge-Kutta Method)')
plt.legend()
plt.grid()
plt.show()


# In[ ]:





# In[ ]:




