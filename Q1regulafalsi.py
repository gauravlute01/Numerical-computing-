def regula_falsi_method(func, a, b, tol=1e-6, max_iter=1000):
    if func(a) * func(b) >= 0:
        print("Regula falsi method fails.")
        return None

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2

