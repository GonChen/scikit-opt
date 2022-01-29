if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.getcwd())

import matplotlib.pyplot as plt
from functools import partial
import numpy as np
from plot_3d import my_plot_3d
from my_demo_func import *


# demo_func = my_sphere
# demo_func = partial(my_rosenbrock, a=-1, b=100)
# demo_func = my_rastrigin
# demo_func = my_booth
# demo_func = my_matyas
# demo_func = my_ackley
# demo_func = my_levi13
# demo_func = my_himmelblau
# demo_func = my_beale
demo_func = my_goldstein_price

X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
import sys,os
print(os.environ.get('PYTHONPATH'))
print(sys.path)
from sko.PSO import PSO
pso = PSO(func=demo_func, n_dim=2, pop=40, max_iter=20, lb=[-5, -5], ub=[5, 5], w=0.8, c1=0.5, c2=0.5, record_mode=True)
pso.run()
my_plot_3d(demo_func, X, Y, record=pso.record_value)
print('best_x is ', pso.gbest_x, 'best_y is', pso.gbest_y)
