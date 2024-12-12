#newton Raphson 
import matplotlib.pyplot as plt
import numpy as np
real_points = np.linspace(0,5,20)
imag_points = np.linspace(0,5,20)

for Im in imag_points :
    for Re in real_points :
        z= Re + Im*1j
        root = newtonraphson(z)
        roots.append(root)

color= []
for root in roots :
    if abs(root -(-.5 + .86j)) < .01 :
        colors.append('red')
    elif abs(root -(-.5 - .86j)) < .01 :
        colors.append('blue')
    else:
        colors.append('black')
x,y = np.meshgrid(real_points,imag_points)
plt.scatter (x,y ,roots,points, imag_points, 

