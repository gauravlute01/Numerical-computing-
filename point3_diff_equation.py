# the third point first difference formula 

def f(x):
    return x**2
def forward_difference3(f,x,h):
    return  (1/(h*2))*(-3*f(x)+4*f(x+h)-f(x+2*h))
def backward_difference3(f,x,h):
    return (1/(h*2))*(f(x-2*h)-(4*f(x-h))+(3*f(x)))
def central_difference3(f,x,h):
    return (f(x+h) -f(x-h)) / (2*h)
result1=forward_difference3(f,2,0.1)
result2=backward_difference3(f,2,0.1)
result3=central_difference3(f,2,0.1)
print(result1,result2,result3)



#  3 point second differentation forward, backward ,central
def f(x):
    return 2*x
def forward_difference2(f,x,h):
    return (f(x) - 2*f(x+h) + f(x+2*h)) / (h**2)
def backward_difference2(f,x,h):
    return (f(x-2*h) - 2*f(x-h) + f(x)) / (h**2)
def central_difference2(f,x,h):
    return (f(x-h) - 2*f(x) + f(x+h)) / (h**2)
result1=forward_difference2(f,2,0.1)
result2=backward_difference2(f,2,0.1)
result3=central_difference2(f,2,0.1)
print(result1,result2,result3)


