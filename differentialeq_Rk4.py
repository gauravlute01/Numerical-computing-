#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt

# Equation
def fun(x, v, t, delta, alpha, beta, gamma, omega):
    dxdt = v
    dvdt = -delta * v - alpha * x - beta * x**3 + gamma * np.cos(omega * t)
    return dxdt, dvdt

# parameters
t0 = 0
tf = 60
dt = 0.01
n = int((tf - t0) / dt) + 1



# RK4
def rk_4(n, x0, v0, t0, tf, dt, delta, alpha, beta, gamma, omega):
    t = np.linspace(t0, tf, n)
    x = np.zeros(n)
    v = np.zeros(n)
    
    x[0] = x0
    v[0] = v0
    
    for i in range(1, n):
        h = t[i-1]
        k1x, k1v = fun(x[i-1], v[i-1], h, delta, alpha, beta, gamma, omega)
        k2x, k2v = fun(x[i-1] + 0.5 * dt * k1x, v[i-1] + 0.5 * dt * k1v, h + 0.5 * dt, delta, alpha, beta, gamma, omega)
        k3x, k3v = fun(x[i-1] + 0.5 * dt * k2x, v[i-1] + 0.5 * dt * k2v, h + 0.5 * dt, delta, alpha, beta, gamma, omega)
        k4x, k4v = fun(x[i-1] + dt * k3x, v[i-1] + dt * k3v, h + dt, delta, alpha, beta, gamma, omega)

        x[i] = x[i-1] + (dt / 6) * (k1x + 2 * k2x + 2 * k3x + k4x)
        v[i] = v[i-1] + (dt / 6) * (k1v + 2 * k2v + 2 * k3v + k4v)

    return t, x, v

# cases
cases = [
    {'delta': 0, 'alpha': -1, 'beta': 1, 'gamma': 0, 'omega': 5, 'x0': -1, 'v0': 1, 'name': 'Case 1'},
    {'delta': 0, 'alpha': -1, 'beta': 1, 'gamma': 0, 'omega': 5, 'x0': -1.414, 'v0': 0, 'name': 'Case 2'},
    {'delta': 0.1, 'alpha': -1, 'beta': 1, 'gamma': 0.34, 'omega': 1.4, 'x0': 0, 'v0': 0, 'name': 'Case 3'}]
 
# Plot
def plot(t, x, v,name):
    plt.figure(figsize=(20, 6))
    
    # Plot x vs time
    plt.subplot(1, 4, 1)
    plt.plot(t, x)
    plt.xlabel('Time (t)')
    plt.ylabel('x')
    plt.title(f'Time vs x ({name})')
    
    # Plot v vs time
    plt.subplot(1, 4, 2)
    plt.plot(t, v)
    plt.xlabel('Time (t)')
    plt.ylabel('v')
    plt.title(f'Time vs v ({name})')
    
    # Plot v˙ vs time
    dvdt = np.gradient(v, t)
    plt.subplot(1, 4, 3)
    plt.plot(t, dvdt)
    plt.xlabel('Time (t)')
    plt.ylabel('v˙')
    plt.title(f'Time vs v˙ ({name})')
    
    # Plot phase space (x vs v)
    plt.subplot(1, 4, 4)
    plt.plot(x, v)
    plt.xlabel('x')
    plt.ylabel('v')
    plt.title(f'Phase Space: x vs v ({name})')
    
    plt.suptitle(f'Case: {name}')
    plt.tight_layout()
    plt.show()

# result in 60 sec
for i in cases:
    t, x, v = rk_4(n, i['x0'], i['v0'], t0, tf, dt, i['delta'], i['alpha'], i['beta'], i['gamma'], i['omega'])
    plot(t, x, v, i['name'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




