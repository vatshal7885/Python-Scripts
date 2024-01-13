import numpy as np            
import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib.cm as cm
rcParams['figure.figsize'] =5,6
from scipy import integrate
import progressbar
plt.rcParams.update({'font.size': 18})
plt.rcParams['font.sans-serif'] = "Georgia"
# Then, "ALWAYS use sans-serif fonts"
plt.rcParams['font.family'] = "Georgia"


global d, l, rho
d =11       #defining the dimension of the hilbert space

#counts in standard basis

N = np.random.rand(d,d)  #taking a random set of data

rho = N/(sum(sum(N))) #rho elements in the standard basis
plt.matshow(N)
plt.show()

rhodiag = np.diagonal(N) #diagonal elemets of rho in standard basis

l = np.sqrt(rhodiag/(sum(rhodiag))) #lambdas

#calculation of F1
F1l = l**2*rhodiag
F1 = sum(F1l) #F1 in the fidelity equation

N1 = np.random.rand(d,d) #counts in tilted or MUB basis
plt.matshow(N1)
plt.show()

c = N.dot(l)
cl = d**2/(sum(l))**2*(l.dot(c))


rho1 = N1/(sum(sum(N1)))*cl #rho elements in the tilted basis

#Calculation of F2
######################################################
def gam(m,n,m1,n1):
    if((m-m1+n1-n)%d == 0):
        return np.sqrt(l[m]*l[n]*l[m1]*l[n1])
    else:
        return 0
    
def sumpara(m,n,m1,n1):
    if(m!=m1 & m!=n & n!=n1 & m1!=n1):
        return 1
    else:
        return 0
######################################################

F2a = (sum(l))**2/d*sum(np.diagonal(rho1))

F2b = -l.dot(N.dot(l))

f2c = 0

for m in range(d):
    for n in range(d):
        for m1 in range(d):
            for n1 in range(d):
                f2c += sumpara(m,n,m1,n1)*gam(m,n,m1,n1)*np.sqrt(rho[m,n]*rho[m1,n1])

F2c = -f2c

F2 = F2a + F2b + F2c

Fbound = F1 + F2

print("The fidelity bound")
print(Fbound)


#calculation of Bks (entanglement dimensionality)

def B(k):
    la = 0
    for i in range(k):
        la+= (l[i])**2
    return la
k = 1
d1 = d*1.0
while(k < d1 & F2 <= B(k-1)):
    k = k+1



print("The dimension of the entanglement")
print(k)

