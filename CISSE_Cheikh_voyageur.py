import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd
import numpy.linalg as la
from math import *

def distance_ville(v1,v2):
    return  sqrt(((v1[0] - v2[0])**2)+((v1[1] - v2[1])**2))

def trajet(n):
    return rd.rand(n,2)

def distance_trajet(trajet):
    s = 0
    n = len(trajet)
    for i in range(n-1):
        s+= distance_ville(trajet[i], trajet[i+1])
    s+=distance_ville(trajet[n-1], trajet[0])
    return s

def Q(trajet):
    n = len(trajet)
    X = trajet.copy()
    i= rd.choice(n)
    while True:
        j = rd.choice(n)
        if i!=j :
            trajet[i] = X[j]
            trajet[j] = X[i]
            break
    return trajet.copy()

def temperature(i):
    Lambda = 1
    return pow(Lambda,i)

def recuit_simule(trajet,m):
    n = len(trajet)
    y = trajet
    for i in range(m):
        y = Q(trajet)
        if rd.uniform() < exp((distance_trajet(trajet) - distance_trajet(y))/temperature(i)):
            trajet = y
    return y

def plot_trajet(trajet):
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot()
    for i in range(len(trajet) - 1):
        ax.scatter(trajet[i][0], trajet[i][1], color = "red", marker = "o")
    ax.scatter(trajet[9][0], trajet[9][1], color = "red", marker = "o")
    for i in range(len(trajet) - 1):
        ax.plot([trajet[i][0], trajet[i+1][0]], [trajet[i][1], trajet[i+1][1]], color = "blue")
    ax.plot([trajet[9][0], trajet[0][0]], [trajet[9][1], trajet[0][1]], color = "blue")
    fig.canvas.draw()
    plt.show()
    
def main():
    N = 10 # nombres de villes
    n = 100000 #nombres de simulaton du recuit 
    M = trajet(N)
    T = recuit_simule(M,n)
    print(distance_trajet(M))
    print(distance_trajet(T))
    plot_trajet(M)
    plot_trajet(T)
   
   
    
    
if __name__ == main():
    main()