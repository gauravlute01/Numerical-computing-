# given function 
x = [0,0.5,1,2]
# interpolating function 
y= [1,1.8987,3.7183,11.3891]
# interploting value 
t = 1.5
# create function 
def newton_divided_difference(x, y, t):
    p = [y[0]]
    for i in range(1, len(x)):
        # Initialize the term
        term = y[i]
        for j in range(i):
            term = (term - p[j]) / (x[i] - x[j])

        # Add the term to the polynomial
        p.append(term)

    # Evaluate the polynomial at t
    result = 0
    for i in range(len(x)):
        term = p[i]
        for j in range(i):
            term *= (t - x[j])
        result += term

    return result



result = newton_divided_difference(x, y, t)
print('value of interpolating function::',result)

