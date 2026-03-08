import matplotlib.pyplot as plt
import numpy as np
import sympy as sp # importing modules

upper_lim = 100
fig, axs = plt.subplots() #Defining the plot
axs.axline((-upper_lim,-upper_lim),slope=1)
axs.set_xlim(-upper_lim,upper_lim)
axs.set_ylim(-upper_lim+100,upper_lim+100)

plt.show()