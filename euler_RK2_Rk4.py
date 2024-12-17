#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a program to solve the differential equation  using RK2 and RK4 method.
#Solve simple pendulum using the Euler, RK2 and RK4 method for same value of h.


# In[22]:


# simple pendulum euler method 
# theta = -(g/l) sin(theta)
# split 
# w' = -(g/l) sin (theta)
# theta' = w 
###################
import math
def f_omega(theta, l=1):
    return -(9.81/l)*math.sin(theta)
def f_theta(omega):
    return omega
# --------
N = 1000
h = 0.01
def euler_method(h,N):
    # arrays 
    omega = [0]*N
    theta = [0]*N

    theta[0] = 1
    omega[0] = 1
    for i in range(1,N):
        omega[i] = omega[i - 1] + h*f_omega(theta[i-1])
        theta[i] = theta[i - 1] + h*f_theta(omega[i-1])
    return  theta
#print(euler_method(h,N))
result = euler_method(h,N)
import matplotlib.pyplot as plt
plt.plot(result)
plt.title("Simple Pendulum (euler method)")

# 


# In[38]:


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

# Euler method
def euler_method(theta0, omega0, h, N):
    theta = [0]*N
    omega = [0]*N
    theta[0] = theta0
    omega[0] = omega0
    for i in range(1,N):
        omega[i] = omega[i-1]+h*f_omega(theta[i-1],omega[i-1])
        theta[i] = theta[i-1]+h*f_theta(theta[i-1],omega[i-1])
    return theta, omega

# RK2 method 
def rk2_method(theta0, omega0, h, N):
    theta = [0]*N
    omega = [0]*N
    theta[0] = theta0
    omega[0] = omega0
    for i in range(1, N):
        k1_theta = h*f_theta(theta[i-1],omega[i-1])
        k1_omega = h*f_omega(theta[i-1],omega[i-1])
        k2_theta = h*f_theta(theta[i-1]+k1_theta/2,omega[i-1]+k1_omega/2)
        k2_omega = h*f_omega(theta[i-1]+k1_theta/2,omega[i-1]+k1_omega/2)
        theta[i] = theta[i-1]+k2_theta
        omega[i] = omega[i-1]+k2_omega
    return theta,omega

# RK4 method
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


# call function 
theta_euler, omega_euler = euler_method(theta0, omega0, h, N)
theta_rk2, omega_rk2 = rk2_method(theta0, omega0, h, N)
theta_rk4, omega_rk4 = rk4_method(theta0, omega0, h, N)

# Plots
t = np.arange(0,N*h,h)
plt.figure(figsize=(12,8))
plt.plot(t,theta_euler,label='Euler Method')
plt.plot(t,theta_rk2,label='RK2 Method')
plt.plot(t,theta_rk4,label='RK4 Method')
plt.title('Simple Pendulum')
plt.xlabel('Time')
plt.ylabel('Angle')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




