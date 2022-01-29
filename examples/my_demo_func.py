import numpy as np
import math

def my_sphere(x):
    x1, x2 = x
    return x1 ** 2 + x2 ** 2

def my_rosenbrock(xy, a=2, b=5):
    x, y = xy
    return (a - x) ** 2 + b * ((y - x ** 2) ** 2)

def my_rastrigin(xy):
    x, y = xy
    return 10 * 2 + (x ** 2 - 10 * np.cos(2 * math.pi * x)) + (y ** 2 - 10 * np.cos(2 * math.pi * y))

def my_booth(xy):
    x, y = xy
    # min(1, 3) = 0
    z = (x + 2*y - 7)**2 + (2*x + y - 5)**2
    return z

def my_matyas(xy):
    x, y = xy
    # min(0, 0) = 0
    z = 0.26*(x**2 + y**2) - 0.48*x*y
    return z

def my_ackley(xy):
    x, y = xy
    # min(0, 0) = 0
    z = -20*np.exp(np.fabs(-0.2*np.sqrt(0.5*(x**2 + y**2)))) - np.exp(np.fabs(0.5*(np.cos(2*x*math.pi) + np.cos(2*y*math.pi)))) + math.e + 20
    return -z

def my_levi13(xy):
    x, y = xy
    # min(1, 1) = 0
    z = (np.sin(3*x*math.pi))**2 + ((x - 1)**2)*(1 + np.sin(3*y*math.pi)**2) + ((y - 1)**2)*(1 + np.sin(2*y*math.pi)**2)
    return z

def my_himmelblau(xy):
    x, y = xy
    # min(3, 2) = 0
    # min(-2.805118, 3.131312) = 0
    # min(-3.779310, -3.283186) = 0
    # min(3.584428, -1.848126) = 0
    z = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    return z

def my_beale(xy):
    x, y = xy
    # min(3, 0.5) = 0
    z = (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2
    return z

def my_goldstein_price(xy):
    x, y = xy
    # min(0, -1) = 3
    z = ((1 + (x + y + 1)**2 * (19 - 14*x + 3*(x**2) - 14*y + 6*x*y + 3*(y**2))) * (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*(x**2) + 48*y - 36*x*y + 27*(y**2))))
    return z