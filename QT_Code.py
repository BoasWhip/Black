# -*- coding: utf-8 -*-

from numpy import pi, e
import numpy as np

import matplotlib as plt
import pandas as pd
from pandas import DataFrame

root5 = np.sqrt(5)
phi = (1 + root5) / 2.
four = phi**4

p = [round(x/8.0,3) for x in range(9)]
q = lambda x, y, z: pi*x / e**y - z
r = lambda x, y: x if x > y else y
s = [1/(phi ** _) for _ in range(5)] + [0.5] + [1 - 1/(phi ** _) for _ in range(5)]
s = list(sorted(set([round(_,11) for _ in s])))

print(s)
print(p)
print(list(q(np.array(p),3,1)))
print(r(12,3))