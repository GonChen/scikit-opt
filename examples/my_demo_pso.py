if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.getcwd())

import matplotlib.pyplot as plt
import numpy as np
from plot_3d import my_plot_3d

def demo_func(x1, x2):
    return x1 ** 2 + (x2 - 0.05) ** 2 + x2 ** 2

X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
import sys,os
print(os.environ.get('PYTHONPATH'))
print(sys.path)
from sko.PSO import PSO
pso = PSO(func=demo_func, n_dim=2, pop=40, max_iter=20, lb=[-5, -5], ub=[5, 5], w=0.8, c1=0.5, c2=0.5, record_mode=True)
pso.run()
my_plot_3d(demo_func, X, Y, record=pso.record_value)
print('best_x is ', pso.gbest_x, 'best_y is', pso.gbest_y)
