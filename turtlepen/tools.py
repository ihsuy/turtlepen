import numpy as np
import matplotlib.pyplot as plt 

from turtlepen import configs

def visualize_trace(tt):
    # given Turtle $tt, this method visualize its trace
    xs, ys = list(zip(*tt.trace))
    plt.figure(figsize=configs.FIGSIZE)
    plt.plot(xs, ys, '.', markersize=configs.MARKERSIZE, color=configs.MARKERCOLOR)
    plt.axis('off')
    plt.show()