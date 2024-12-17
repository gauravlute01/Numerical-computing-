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
