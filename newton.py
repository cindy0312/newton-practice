def first_derivative(f, x):
    """Approximate the first derivative of f at x."""
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def second_derivative(f, x):
    """Approximate the second derivative of f at x."""
    h = 1e-4
    return (
        first_derivative(f, x + h)
        - first_derivative(f, x - h)
    ) / (2 * h)


def optimize(start, f):
    """Find a stationary point of f using Newton's method."""
    if not callable(f):
       raise TypeError(f"Argument is not a function, it is of type {type(f)}")
        
    x = start

    for _ in range(100):
        f1 = first_derivative(f, x)
        f2 = second_derivative(f, x)

        if abs(f2) < 1e-12:
            raise ValueError("The second derivative is too close to zero.")

        new_x = x - f1 / f2

        if abs(new_x - x) < 1e-5:
            return new_x

        x = new_x
        
    if x > 1e7:
       raise RuntimeError(f"At iteration {iter}, optimization appears to be diverging")
        
    import warnings
    if x > 3:
       warnings.warn(f"{x} is greater than 3.", UserWarning)



import numpy as np
import numdifftools as nd

def gradient(f, x):
    """Calculate the gradient of f at x."""
    gradient_function = nd.Gradient(f)
    return gradient_function(x)


def hessian(f, x):
    """Calculate the Hessian of f at x."""
    hessian_function = nd.Hessian(f)
    return hessian_function(x)


def optimize(x0, f):
    """Minimize a multivariate function using Newton's method."""
    x = np.asarray(x0, dtype=float)

    for _ in range(100):
        gradient = gradient(f, x)
        hessian = hessian(f, x)

        new_x = x - np.linalg.solve(hessian, gradient)

        if np.linalg.norm(new_x - x) < 1e-5:
            return new_x

        x = new_x

    raise RuntimeError("Newton's method did not converge.")