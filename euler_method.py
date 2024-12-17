#!/usr/bin/env python
# coding: utf-8

# In[2]:


# simple pendulum euler method 
# theta = -(g/l) sin(theta)
# split 
# w' = -(g/l) sin (theta)
# theta' = w 
###################\
import math
def f_omega(theta, l=1):
    return -(9.81/l)*math.sin(theta)
def f_theta(omega):
    return omega
# --------
N = 1000
h = 0.01

# arrays 
omega = [0]*N
theta = [0]*N

theta[0] = 1
omega[0] = 1
for i in range(1,N):
    omega[i] = omega[i - 1] + h*f_omega(theta[i-1])
    theta[i] = theta[i - 1] + h*f_theta(omega[i-1])
#print(theta)
#print(omega)
import matplotlib.pyplot as plt
plt.plot(theta)
#plt.plot(omega)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




