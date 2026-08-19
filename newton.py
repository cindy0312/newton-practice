def optimize(start, f):
    h = 1e-8
    x = start
    
    while True:
        f1 = (f(x + h) - f(x)) / h
        f2 = (f(x + h) - 2 * f(x) + f(x - h)) / h**2

        new_x = x - f1 / f2

        if abs(new_x - x) < 0:
            return new_x

        x = new_x