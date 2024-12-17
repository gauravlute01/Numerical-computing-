#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 1000  
h = 0.01  
theta0 = 1  
omega0 = 1


# given function 
def f_theta(theta, omega, l=1):
    return omega

def f_omega(theta, omega, g=9.81, l=1):
    return -(g/l) * math.sin(theta)


def rk4_method(theta0, omega0, h, N):
    theta =[0]*N
    omega = [0]*N
    theta[0] = theta0
    omega[0] = omega0
    for i in range(1,N):
        k1_theta=h*f_theta(theta[i-1],omega[i-1])
        k1_omega=h*f_omega(theta[i-1],omega[i-1])
        k2_theta=h*f_theta(theta[i-1]+k1_theta/2,omega[i-1]+k1_omega/ 2)
        k2_omega=h*f_omega(theta[i-1]+k1_theta/2,omega[i-1]+k1_omega/2)
        k3_theta=h*f_theta(theta[i-1]+k2_theta/2,omega[i-1]+k2_omega/ 2)
        k3_omega=h*f_omega(theta[i-1]+k2_theta/2,omega[i-1]+k2_omega/2)
        k4_theta=h*f_theta(theta[i-1]+k3_theta, omega[i-1]+k3_omega)
        k4_omega=h*f_omega(theta[i-1]+k3_theta, omega[i- 1]+k3_omega)
        theta[i]=theta[i-1]+1/6*(k1_theta+2*k2_theta+2*k3_theta+k4_theta)
        omega[i]=omega[i-1]+1/6*(k1_omega+2*k2_omega+2*k3_omega+k4_omega)
    return theta,omega
theta_rk4, omega_rk4 = rk4_method(theta0, omega0, h, N)
plt.plot(theta_rk4, omega_rk4)


# In[2]:


# adding friction terms

import math
import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 1000  
h = 0.01  
theta0 = 1  
omega0 = 1


# given function 
def f_theta(theta, omega, l=1):
    return omega

def f_omega(theta, omega, g=9.81, l=1):
    return -(g/l) * math.sin(theta)


def rk4_method(theta0, omega0, h, N):
    theta =[0]*N
    omega = [0]*N
    theta[0] = theta0
    omega[0] = omega0
    for i in range(1,N):
        k1_theta=h*f_theta(theta[i-1],omega[i-1])
        k1_omega=h*f_omega(theta[i-1],omega[i-1])
        k2_theta=h*f_theta(theta[i-1]+k1_theta/2,omega[i-1]+k1_omega/ 2)
        k2_omega=h*f_omega(theta[i-1]+k1_theta/2,omega[i-1]+k1_omega/2)
        k3_theta=h*f_theta(theta[i-1]+k2_theta/2,omega[i-1]+k2_omega/ 2)
        k3_omega=h*f_omega(theta[i-1]+k2_theta/2,omega[i-1]+k2_omega/2)
        k4_theta=h*f_theta(theta[i-1]+k3_theta, omega[i-1]+k3_omega)
        k4_omega=h*f_omega(theta[i-1]+k3_theta, omega[i- 1]+k3_omega)
        theta[i]=theta[i-1]+1/6*(k1_theta+2*k2_theta+2*k3_theta+k4_theta)
        omega[i]=omega[i-1]+1/6*(k1_omega+2*k2_omega+2*k3_omega+k4_omega)
    return theta,omega
theta_rk4, omega_rk4 = rk4_method(theta0, omega0, h, N)
plt.plot(theta_rk4, omega_rk4)


# In[6]:


# lorenz attractor
rho = 50
beta = 2.6667
sigma = 10

N = 5000  
h = 0.01  
x0 = 0.2  
y0 = 0.89
z0 = 0.52

def f_x(sigma,x, y,z):
    return sigma*(y - x)
def f_y(rho,x,y,z):
    return x*(rho - z) - y
def f_z(beta,x,y,z):
    return x*y - beta*z

def rk4_method(x0, y0, z0, h, N):
    x =[0]*N
    y = [0]*N
    z = [0]*N
    x[0] = x0
    y[0] = y0
    z[0] = z0
    for i in range(1,N):
        k1_x=h*f_x(sigma,x[i-1],y[i-1],z[i-1])
        k1_y=h*f_y(rho,x[i-1],y[i-1],z[i-1])
        k1_z=h*f_z(beta,x[i-1],y[i-1],z[i-1])
        
        k2_x=h*f_x(sigma,x[i-1]+k1_x/2,y[i-1]+k1_y/ 2,z[i-1]+k1_z/2)
        k2_y=h*f_y(rho,x[i-1]+k1_x/2,y[i-1]+k1_y/2,z[i-1]+k1_z/2)
        k2_z=h*f_z(beta,x[i-1]+k1_x/2,y[i-1]+k1_y/2,z[i-1]+k1_z/2)
        
        k3_x=h*f_x(sigma,x[i-1]+k2_x/2,y[i-1]+k2_y/2,z[i-1]+k2_z/2)
        k3_y=h*f_y(rho,x[i-1]+k2_x/2,y[i-1]+k2_y/2,z[i-1]+k2_z/2)
        k3_z=h*f_z(beta,y[i-1]+k2_x/2,y[i-1]+k2_y/2,z[i-1]+k2_z/2)
        
        k4_x=h*f_x(sigma,x[i-1]+k3_x, y[i-1]+k3_y, z[i-1]+k3_z)
        k4_y=h*f_y(rho,x[i-1]+k3_x, y[i-1]+k3_y, z[i-1]+k3_z)
        k4_z=h*f_z(beta,x[i-1]+k3_x, y[i-1]+k3_y, z[i-1]+k3_z)

        x[i]=x[i-1]+1/6*(k1_x+2*k2_x+2*k3_x+k4_x)
        y[i]=y[i-1]+1/6*(k1_y+2*k2_y+2*k3_y+k4_y)
        z[i]=z[i-1]+1/6*(k1_z+2*k2_z+2*k3_z+k4_z)
    return x, y, z
x_rk4, y_rk4, z_rk4 = rk4_method(x0, y0, z0, h, N)
plt.plot(x_rk4, y_rk4)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




