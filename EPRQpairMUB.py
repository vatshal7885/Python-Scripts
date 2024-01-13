# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:38:44 2020

@author: Vatshal Srivastav
"""
import numpy as np            
import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib.cm as cm
rcParams['figure.figsize'] =5,5

from scipy import integrate
#Sd(import progressbar
plt.rcParams.update({'font.size': 18})
plt.rcParams['font.sans-serif'] = "Georgia"
# Then, "ALWAYS use sans-serif fonts"
plt.rcParams['font.family'] = "Georgia"
def p(d):
    a = 0.5*(1.+ 1./(d**0.5+1))
    return a

def Q(d):
    a = 1 + p(d)*d/(1-p(d))
    return a

def pall(d,l):
    a = (l*d-d-1)/(d**2-1.)
    return a
#n = np.linspace(2,5,4)
l = np.array([2.366,2.618,3.0542,3.4178,3.8966]);
#n = np.array([2,3,4,5,6,7,8,9,10,11,12,13,14,16])
#n = np.array([3])
d = np.array([2,3,5,7,11])*1.0
Qall = 1.0 + d*pall(d,l)/(1.-pall(d,l))
#Q0 = np.zeros(len(n))
#d0 = np.zeros(len(n))
Q2 = Q(d)
plt.plot(d,Q2,label=r'Pair of MUB')
plt.plot(d,Qall,label=r'All MUBs')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
    #plt.legend(r'mu = %s' %round(mu[j],2))
axes = plt.gca()
axes.set_xlim([2, d.max()])
#axes.set_ylim([0, Q2.max()])
    #plt.title(r'$\mu$ = 0.05')
plt.xlabel("d (dimension)")
plt.ylabel(r'$\mathcal{Q}^*$')
plt.show()
    
