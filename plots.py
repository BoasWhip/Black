# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:42:07 2017

@author: ozsanos
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 2*np.pi, 10)
markerline, stemlines, baseline = plt.stem(x, np.cos(x), '-.')
plt.setp(baseline, 'color', 'r', 'linewidth', 2)

plt.show()