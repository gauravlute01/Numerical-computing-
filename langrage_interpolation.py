def lagrange_interpolation(x_value,y_value, x):
    result=0
    for i in range(len(y_value)):
        term = y_value[i]
        for j in range(len(x_value)):
            if j != i :
                term = term * (x - x_value[j] / (x_value[i] - x_value[j] ))
        result += term 
    return result 
# example usage 
x_value=[-1, 1, 2]
y_value=[6, 0,6]

x_to_interpolate = 3
interpolated_value = lagrange_interpolation(x_value,y_value, x_to_interpolate)
print(interpolated_value)
