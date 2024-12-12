import numpy as np

def derivative(func, x, h=1e-6):
    return (func(x + h) - func(x)) / h

def newton_raphson_method(func, x0, tol=1e-6, max_iter=1000):
    iter_count = 0
    while abs(func(x0)) > tol and iter_count < max_iter:
        x0 = x0 - func(x0) / derivative(func, x0)
        iter_count += 1
    return x0

