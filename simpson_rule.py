# simpsons 1/3 method 
def f(x):
    return 1/(1+x**2)
a = int(input("enter your value A:"))
b = int(input("enter your value B:"))
n = int(input("enter number of sub interval:"))
h = (b-a)/n
k = 1
sum = 0
while (k<n):
    x = a+k*h
    if (k%2==0):
        sum = sum+2*f(x)
    else:
        sum = sum+4*f(x)
    k = k+1
ia = (h/3)*(f(a)+f(b)+sum)
print("The value of integration is simpsons 1/3 method:",ia)

