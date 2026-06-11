def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    for i in range(steps):
        d=2*a*x0+b
        x0=x0-lr*d
    return float(x0)
        