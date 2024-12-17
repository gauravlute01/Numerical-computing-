#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
# psuedo code ********
define f(x,t)
input x0, y0, N, h
initialize x[], t[]
    x[0]=x0, t[0]=t0
for loop
for i in range(1,N):
k1 = f(x[i-1],t[i-1])
k2 = f(x[i-1]+(h/2)*k1, t[i-1]+h/2)
k3 = f(x[i-1]+(h/2)*k2, t[i-1]+h/2)
k4 = f(x[i-1]+h*k3, t[i-1])
x[i] = x[i-1] + h/6(k1_2k2+2k3+k4)
'''


# In[22]:


# Runge_kutta method
#create function
import math
def f(x,t):
    return x*t
# Input all values
x0 =1
t0 =1
N = 100
h = 0.01
# initailize all the values
x = [0.0] *N
t = [0.0] *N

x[0] = x0
t[0] = t0
# apply loop 
for i in range(1,N):
    k1 = f(x[i-1], t[i-1])
    k2 = f((x[i-1]+((h/2)*k1)), (t[i-1]+(h/2)))
    k3 = f((x[i-1]+((h/2)*k2)), (t[i-1]+(h/2)))
    k4 = f((x[i-1]+(h*k3)), t[i -1])
    x[i] = x[i-1] + (h/6)*(k1 + (2*k2) + (2*k3) +k4)
#print(x) 
import matplotlib.pyplot as plt 
plt.plot(x)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




