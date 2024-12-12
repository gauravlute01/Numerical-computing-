# First differentiation using five-point formulas

def f(x):
    return x**2

def forward_difference(f, x, h):
    return (1/(12*h)) * (-25*f(x) + 48*f(x + h) - 36*f(x + 2*h) + 16*f(x + 3*h) - 3*f(x + 4*h))

def backward_difference(f, x, h):
    return (1/(12*h)) * (25*f(x) - 48*f(x - h) + 36*f(x - 2*h) - 16*f(x - 3*h) + 3*f(x - 4*h))

def central_difference(f, x, h):
    return (f(x - 2*h) - 8*f(x - h) + 8*f(x + h) - f(x + 2*h)) / (12 * h)

result1 = forward_difference(f, 2, 0.1)
result2 = backward_difference(f, 2, 0.1)
result3 = central_difference(f, 2, 0.1)
print("First Differentiation (Five-point formula):")
print("Forward Difference:", result1)
print("Backward Difference:", result2)
print("Central Difference:", result3)

# Second differentiation using five-point formulas

def forward_difference2(f, x, h):
    return (1/(12*h**2)) * (-f(x) + 16*f(x + h) - 30*f(x + 2*h) + 16*f(x + 3*h) - f(x + 4*h))

def backward_difference2(f, x, h):
    return (1/(12*h**2)) * (-f(x) + 16*f(x - h) - 30*f(x - 2*h) + 16*f(x - 3*h) - f(x - 4*h))

def central_difference2(f, x, h):
    return (f(x - 2*h) - 4*f(x - h) + 6*f(x) - 4*f(x + h) + f(x + 2*h)) / (h**2)

result1 = forward_difference2(f, 2, 0.1)
result2 = backward_difference2(f, 2, 0.1)
result3 = central_difference2(f, 2, 0.1)
print("\nSecond Differentiation (Five-point formula):")
print("Forward Difference:", result1)
print("Backward Difference:", result2)
print("Central Difference:", result3)
