# newton raphson method 
def f(x) :
    return x**3 - 5*x - 9 
def g(x):
    return 3*x**2 - 5
a = float(input("Enter intial value ::"))
iter = 0
while True :
    iter += 1
    c = a-(f(a)/g(a))
    # check if the absolute value of f(c) is less than the tolerance 
    if abs(f(c))<0.00001:
        break 
    # update the value of a for the next iteration 
    a = c
print(f"The value of the root :{c}, f(c) :{f(c)}, and it required iteration :{iter}")

