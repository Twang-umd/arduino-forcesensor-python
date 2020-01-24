# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:20:37 2020

@author: tomwtn
"""

"""
plot exercise
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes



plt.plot(range(10))
plt.savefig('testplot02.jpg',dpi=400)

