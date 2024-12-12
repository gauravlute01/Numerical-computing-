# secant method 
def f(x):
    return x**3 - 5*x -9
def secant_method(a, b, N):
    iter = 0
    for i in range(N):
        iter += 1
        c = b -(b - a) * f(b) / (f(b) - f(a))
        if abs(f(c))<0.00001:
            break 
        a = b 
        b = c
    return c, iter
a = float(input("Enter your bracketed root a: "))
b = float(input("Enter your bracketed root b: "))
iterations = int(input("Enter maxno of iteration:"))
result, num_iterations = secant_method(a, b, iterations)
print(f"The value of the root: {result}, f(c): {f(result)} and it required iterations : {num_iterations}")

