# Trapizodal method interpolation 
def f(x):
    return 1/(1+x**2)
a = int(input("Enter your value A:"))
b = int(input("Enter your value B:"))
n = int(input("Enter number of sub interval:"))
h = (b- a)/n
k = 1
sum = 0
while (k<n):
    t = a+k*h
    sum = sum +f(t)
    k = k+1
    int_a = (h/2)*(f(a)+f(b)+2*sum)
print("The value of integration is trapizodal method:",int_a)

