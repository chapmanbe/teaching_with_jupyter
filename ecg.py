import pandas as pd
import matplotlib.pyplot as plt
import os
from ipywidgets import interact, interactive, fixed
from IPython.display import clear_output, display
import ipywidgets as widgets
import numpy as np

def get_series(f):
    
    data = \
    pd.read_table(f, header=None).apply(
        lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
    return data
def _view_series(root="", f="", num_points=200, color="red"):
    data = get_series(os.path.join(root,f))
    plt.plot(data[1][:num_points], color=color)
    plt.show()