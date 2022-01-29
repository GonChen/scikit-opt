import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def my_plot_3d(func, x_range, y_range, record=None):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # Make data.
    X, Y = np.meshgrid(x_range, y_range)
    Z = func((X, Y))

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, rstride = 1, cstride = 1, linewidth=0, antialiased=False, alpha=0.5)
    if record is not None:
        x_records = record['X']
        y_records = record['Y']
        x_len = len(record['X'])
        from sklearn.preprocessing import minmax_scale
        num_points = x_records[0].shape[0]
        num_points = 20
        colors = minmax_scale(np.array(range(num_points+1)), feature_range=(0, 1))
        cmap = cm.viridis

        for i in range(2, x_len):
            for j in range(num_points):
                xs = np.array(list(map(lambda x: x[j][0], x_records)))
                ys = np.array(list(map(lambda x: x[j][1], x_records)))
                zs = np.array(list(map(lambda y: y[j][0], y_records)))
                xs = xs[i-2:i]
                ys = ys[i-2:i]
                zs = zs[i-2:i]
                ax.plot(xs, ys, zs, lw=1, color=cmap(colors[j]))
                ax.scatter(xs[1], ys[1], zs[1], s=5, color=cmap(colors[j]))
            plt.pause(1)
        #I will replace this line with:
        # a = Arrow3D([mean_x, v[0]], [mean_y, v[1]], 
        #             [mean_z, v[2]], mutation_scale=20, 
        #             lw=3, arrowstyle="-|>", color="r")
        # ax.add_artist(a)
    plt.show()