import math
from time import time
import matplotlib.pyplot as plt
from random import randrange
import numpy as np

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
def first_test(N):
    if N <= 1:
        return False
    for i in range(2,math.floor(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

#2.b
# complexité linéaire O(sqrt(n))

#2.c
def count_prime(K=100000):
    cnt = 0
    for i in range(1,K):
        if first_test(i):
            cnt += 1
    return cnt

#2.d nom changé pour les différencier
def gen_carmichaels(K=100000, p=128):
    #2,3 sont premiers et besoin de n > 2 pour le tirage
    for n in range(4,K):
        if not first_test(n):
            test=True
            for i in range(p):
                a = randrange(2,n)
                if my_pgcd(n,a)==1 and pow(a,n-1,n)!=1:
                    test=False
                    break
            if test:
                yield n
            
#2.e à revoir
def gen_carmichael(K=100000):
    arr = []
    car = list(gen_carmichaels(pow(K,3)))
    # prod = -1
    # for i in range(K):
    #     if first_test(i):
    #         arr.append(i)
    # while prod not in car:
    #     if prod != -1:
    #         arr.remove(a)
    #         arr.remove(b)
    #         arr.remove(c)
    #     np.random.shuffle(arr)
    #     a,b,c = arr[:3]
    #     prod = a*b*c
    #     print(a,b,c)
    return np.random.choice(car,1)[0]
                
#2.f faire tourner 5min et dire cb trouvés








#todo utiliser my expo mod
#Exercice 3
#3.a
def test_fermat(n, p=128):
    for i in range(p):
        a = randrange(2,n)
        if my_pgcd(n,a)==1 and pow(a,n-1,n)!=1:
            return False
    return True

#3.b
def gen_comp(K=100000):
    for i in range(3,K):
        if not first_test(i):
            yield i

def test_test_fermat(K=100000, N=1000):
    p_car = 0
    p_comp = 0
    p_rand = 0
    # à voir le param
    car=list(gen_carmichaels(K))
    comp=list(gen_comp(K))
    for i in range(N):
        if test_fermat(int(np.random.choice(car,1)[0])):
            p_car += 1/N
    for i in range(K):
        if test_fermat(int(np.random.choice(comp,1)[0])):
            p_comp += 1/N
    for i in range(N):
        if test_fermat(randrange(3,K)):
            p_rand += 1/N
    plt.bar(2,p_car,1,label="Carmichael "+str(p_car))
    plt.bar(4,p_comp,1,label="Composé "+str(p_comp))
    plt.bar(6,p_rand,1,label="Random "+str(p_rand))
    plt.title("Probabilité de reconnaissance d'un nombre")
    plt.legend()
    plt.show()



#3.c



#Exercice 4
#4.a
def test_miller_rabin(n, T):
    a = randrange(2,n)
    b = pow(a,m,n)
    if b!= 1 and b!= n-1:
        j = 1
        while j < h and b != n-1:
            if (b*b)%n == 1:
                return False
            b = (b*b)%n
            j = j+1
        if b != n-1:
            return False
    return True
