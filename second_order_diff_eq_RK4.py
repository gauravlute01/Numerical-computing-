#Solving 2nd order differential equation by using RK4 and plotting the results for each case.
import numpy as np
import matplotlib.pyplot as plt

# Parameters and initial conditions for the differential equation 
initialvalues = [(0, -1, 1, 0, 5, -1, 1, 1), (0, -1, 1, 0, 5, -1.414, 0, 2), (0.1, -1, 1, 0.34, 1.4, 0, 0, 3)]


for delta, alpha, beta, gamma, omega, x0, v0, case in initialvalues:

    #initial conditions
    t0 = 0
    tfinal = 60 #running simulation for 60 seconds
    dt = 0.01
    n = int((tfinal - t0) / dt)  #splitting into n number of steps according to change in time.
    t_values = np.linspace(t0, tfinal, n) #creating number of parts as per steps.

    t_values = np.linspace(t0, tfinal, n)
    x_values = np.zeros(n)
    v_values = np.zeros(n)
    vdot_values = np.zeros(n)

    # Initial values
    x_values[0] = x0
    v_values[0] = v0

    #defining functions
    def f_x(v):
        return v

    def f_v(t, x, v):
        return -delta * v - alpha * x - beta * x**3 + gamma * np.cos(omega * t)

    def f_theta(omega):
        return omega

    #RK4
    for i in range(1, n):
        t = t_values[i-1]
        x = x_values[i-1]
        v = v_values[i-1]
        
        k1_x = dt * v
        k1_v = dt * f_v(t, x, v)
        
        k2_x = dt * (v + 0.5 * k1_v)
        k2_v = dt * f_v(t + 0.5 * dt, x + 0.5 * k1_x, v + 0.5 * k1_v)
        
        k3_x = dt * (v + 0.5 * k2_v)
        k3_v = dt * f_v(t + 0.5 * dt, x + 0.5 * k2_x, v + 0.5 * k2_v)
        
        k4_x = dt * (v + k3_v)
        k4_v = dt * f_v(t + dt, x + k3_x, v + k3_v)
        
        x_values[i] = x + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        v_values[i] = v + (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
        vdot_values[i] = f_v(t, x_values[i], v_values[i])


    #Time vs x
    plt.subplot(2, 2, 1)
    plt.plot(t_values, x_values, label='$x(t)$', color='orange')
    plt.xlabel('Time (t)')
    plt.ylabel('$x$')
    plt.title(f'Time vs $x$   for case ={case}')
    plt.grid(True)
    plt.legend()

    # Time vs v
    plt.subplot(2, 2, 2)
    plt.plot(t_values, v_values, label='$v(t)$', color='red')
    plt.xlabel('Time (t)')
    plt.ylabel('$v$')
    plt.title(f'Time vs $v$  for case ={case}')
    plt.grid(True)
    plt.legend()

    # Time vs vdot
    plt.subplot(2, 2, 3)
    plt.plot(t_values, vdot_values, label='$\dot{v}(t)$', color='green')
    plt.xlabel('Time (t)')
    plt.ylabel('$\dot{v}$')
    plt.title(f'Time vs vdot  for case ={case}')
    plt.grid(True)
    plt.legend()

    # Phase space: x vs v
    plt.subplot(2, 2, 4)
    plt.plot(x_values, v_values, label='Phase Space ($x$ vs $v$)', color='magenta')
    plt.xlabel('$x$')
    plt.ylabel('$v$')
    plt.title(f'Phase Space: $x$ vs $v$   for case ={case}')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
