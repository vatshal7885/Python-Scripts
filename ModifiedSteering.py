# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:37:47 2020

@author: Vatshal Srivastav
"""

import numpy as np            
import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib.cm as cm
rcParams['figure.figsize'] =10,6
from scipy import integrate
#Sd(import progressbar
plt.rcParams.update({'font.size': 18})
plt.rcParams['font.sans-serif'] = "Georgia"
# Then, "ALWAYS use sans-serif fonts"
plt.rcParams['font.family'] = "Georgia"

def eta(p,d):
    m = d+1
    a = (1+m*(d**0.5+1))/m/(p + (1-p)/d)- (d**0.5+1)
    return a

def Q(p,d):
    a = 1 + p*d/(1-p)
    return a
  
    
p = np.linspace(0,1,100)
d = np.array([3,5,7, 11, 13])*1.0

for i in range(len(d)):
    Q1 = Q(p,d[i])
    eta1 = eta(p,d[i])
    plt.plot(eta1,Q1, label =r'd = %s' %d[i])

plt.legend(bbox_to_anchor=(0.7, 1), loc=2, borderaxespad=0.)
plt.xlabel("$\eta$")
plt.ylabel(r'$\mathcal{Q}^*$')
axes = plt.gca()
axes.set_xlim([0, 1])





