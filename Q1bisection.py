def bisection_method(func, a, b, tol=1e-6, max_iter=1000):
    if func(a) * func(b) >= 0:
        print("Bisection method fails.")
        return None

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint
        elif func(midpoint) * func(a) < 0:
            b = midpoint
        else:
            a = midpoint
        iter_count += 1

    return (a + b) / 2

