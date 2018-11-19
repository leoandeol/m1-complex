import math
from time import time
import matplotlib.pyplot as plt
from random import randrange

#1.a
def my_pgcd(a,b):
    # algo euclide
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b
#1.b
def algo_euc_et(a,b):
    u = [1,0]
    v = [0,1]
    r = [a,b]
    i = 1
    while r[i] != 0:
        qi = r[i-1]//r[i]
        ri_1 = r[i-1] % r[i]
        r.append(ri_1)
        ui_1 = u[i-1] - (qi*u[i])
        u.append(ui_1)
        vi_1 = v[i-1] - (qi*v[i])
        v.append(vi_1)
        i += 1
    return r[i-1],u[i-1],v[i-1]
    
def my_inverse(a,N):
    r, u, v = algo_euc_et(a,N)
    if r != 1:
        return "Erreur"
    else:
        return u

#1.3c
def est_complexity():
    t_pgcd = []
    t_inv = []
    l_k = []
    for i in range(2,20):
        k = pow(10,i)
        l_k.append(k)
        start = time()
        [my_pgcd(k-1,randrange(pow(10,i-1),k-1)) for _ in range(1000)]
        end = time()
        t_pgcd.append(end-start)
        start = time()
        [my_inverse(randrange(pow(10,i-1),k-1),k-1) for _ in range(1000)]
        end = time()
        t_inv.append(end-start)
    plt.plot(l_k, t_pgcd, 'r')
    plt.plot(l_k, t_inv, 'b')
    plt.show()

#1.d
def my_expo_mod(g,n,N):
    h = 1
    for i in range(math.floor(math.sqrt(n)),-1,-1):
        h = pow(h,2) % N
        if bin(n)[2:][-i]:
            h = h*g % N
    return h

#2.a
