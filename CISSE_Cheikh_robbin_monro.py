import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd
from math import *


def monro(theta0,gamma,X,Y):
    theta = np.asarray(theta0)
    for i in range(1,len(X)):
        theta = theta - gamma(i+1)*np.array([-2*X[i]*(Y[i] - (theta[0]*X[i] + theta[1])), 
                                             -2*Y[i] + 2*theta[0]*X[i]+ 2*theta[1]])
    return theta

def main():
    gamma1 = lambda n : .2/(n+1)
    gamma2 = lambda n: 1.3/(n+1)
    U = np.loadtxt("TP4-exo2.txt")
    X = U[:,0]
    Y = U[:,1]
    n = len(X)
    theta0 = [1,1]
    Gamma = [gamma1,gamma2]
    for gamma in Gamma:
        theta = monro(theta0,gamma,X,Y)
        Y_estim = theta[0]*X + theta[1]
        plt.scatter(X,Y_estim)
        plt.show()
    #comparaison avec l'estimateur des moindres carres
    theta = monro(theta0,gamma1,X,Y)
    n = len(X)
    X_estim = (Y_estim - theta[1])/theta[0]
    s1 = s2 = 0
    Y_barre = sum(Y)/len(Y)
    X_barre = sum(X)/len(X)
    for i in range(n):
        s1 +=((X[i] - X_barre)*(Y[i] - Y_barre))
        s2+=(X[i] -X_barre)**2
    a_estim = s1/s2
    b_estim = Y_barre - a_estim*X_barre
    estim_moindre_carre = np.array([a_estim,b_estim])
    print("\n")
    print("Comparaison des deux estimations\n")
    print("="*40)
    print("estimation moindre carre : ",estim_moindre_carre)
    print("="*40)
    print("estimation par robin monro",theta)
    print("="*40)
    print("l'erreur entre les  deux estimations est : ", abs(theta - estim_moindre_carre))
    print("="*40)
    
if __name__ == main():
    main()