import numpy as np            
import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib.cm as cm
rcParams['figure.figsize'] =6,10
from scipy import integrate
#Sd(import progressbar
plt.rcParams.update({'font.size': 18})
plt.rcParams['font.sans-serif'] = "Georgia"
# Then, "ALWAYS use sans-serif fonts"
plt.rcParams['font.family'] = "Georgia"
def f(n,d):
    a = ((d + d**0.5-1)*n**0.5 - 1)/(d-1)/(n**0.5+1)
    return a

def Q(n,d):
    a = 1 + f(n,d)*d/(1-f(n,d))
    return a

#n = np.linspace(2,5,4)

n = np.array([2,3,4,5,6,7,8,9,10,11,12,13,14,16])
#n = np.array([3])
d = np.linspace(4,31,28)
Q0 = np.zeros(len(n))
d0 = np.zeros(len(n))
for i in range(len(n)):
    d = np.linspace(n[i]+1,31,31-n[i])
    plt.plot(d,Q(n[i],d), label =r'n = %s' %(n[i]+1))
    d0[i] = d[0]
    Q0[i] = Q(n[i],d[0])
    
plt.plot(d0,Q0, '--x')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
    #plt.legend(r'mu = %s' %round(mu[j],2))
axes = plt.gca()
axes.set_xlim([3, d.max()])
axes.set_ylim([0, Q0.max()])
    #plt.title(r'$\mu$ = 0.05')
plt.xlabel("d (dimension)")
plt.ylabel(r'Q')
plt.show()
    