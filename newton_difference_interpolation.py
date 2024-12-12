# newton difference interpolation 
def divided_defference(x, y):
    n = len(x)
    F = [[0]*n for _ in range(n)]

    for i in range(n):
        F[i][0]=y[i]

    for j in range(1, n):
        for i in range(n-j):
            F[i][j] =(F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])
    return F

def newton_interpolation(x, y, target):
    n = len(x)
    result = y[0]
    F = divided_defference(x, y)

    for i in range(1, n):
        term = F[0][i]
        for j in range(i):
            term *= (target - x[j])
        result += term 
    return result
# given data 
x_values = [0, 0.5, 1, 2]
y_values = [1, 1.8987, 3.7183, 11.3891]

# Target Value
target_value = 1.5

# calculate interpolation 
result = newton_interpolation(x_values, y_values, target_value)
print(f"p(1.5) = {result}")

