# Regula falsi method 
def f(x):
    return x**2 -2
a = int(input("enter your value A:"))
b = int(input("enter your value B:"))
iter = 0
if f(a)*f(b)<0:
    while True:
        iter += 1
        c = ((a*f(b) - b*f(a))/(f(b) - f(a)))
        if f(a)*f(c)<0 :
            b = c
        else:
            a = c
        if abs(f(c))<0.00001:
            break 
    print(f"the value of root:{c} and f(c):{f(c)},requred iteration:{iter}")
else:
    print("Root not bracted")
