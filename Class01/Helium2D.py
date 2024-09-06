#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:54:31 2024

@author: pdam-linux

Helium Atom 2d
"""

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

class proton:
    charge = 2
    def __init__(self,x_position,y_position):
        self.x = x_position
        self.y = y_position
        
class electron:
    charge = -1
    def __init__(self,x_position,y_position):
        self.x = x_position
        self.y = y_position
        

def Mov_part(part):
    """
    This moves a particle in 2 d
    """
    xo = part.x
    yo = part.y

    xn = xo + rand()-0.5
    yn = yo + rand()-0.5
    part.x = xn
    part.y = yn
    return(xn,yn)

def Energy (part_set):
    """
    This func computes the potential energy of the particles set
    """
    E = 0

    for i in part_set:
        x1,y1 = i.x, i.y
        for j in part_set:
            if i == j: continue
            x2,y2 = j.x, j.y

            R = np.sqrt((x1-x2)**2+(y1-y2)**2)
            E += 1/R*(i.charge*j.charge)
    return(E*0.5)


def Monte_Carlo (system,N=500):
    
    e1 = []
    e2 = []
    
    E0 = abs(Energy(system))
    
    i = 0
    
    while i < N:
        opts = [1,2]
        part = int(np.random.choice(opts))
        xt = system[part].x
        yt = system[part].y
    
        Mov_part(system[part])
    
        En = abs(Energy(system))
    
        if (En < E0+0.05*E0) and (En > E0-0.05*E0) or rand()>0.99:
            e1.append([system[1].x,system[1].y])
            e2.append([system[2].x,system[2].y])
            i+=1
        else:
            system[part].x = xt
            system[part].y = yt
        
    return e1,e2

        
if __name__ == '__main__':

    
    E1 = []
    
    E2 = []
    
    for i in range(1000):
        
        proton_a = proton(0,0)
        electron_b = electron(0,-1)
        electron_c = electron(0,1)
        system = [proton_a,electron_b,electron_c]
        e1,e2 = Monte_Carlo(system)
        
        Ea_temp = []
        Eb_temp = []
        
        for ele in e1:
            Ea_temp.append(np.sqrt(ele[0]**2+ele[1]**2))
        
        for ele in e2:
            Eb_temp.append(np.sqrt(ele[0]**2+ele[1]**2))
        
        if max(Ea_temp)>max(Eb_temp):
            E1+=Ea_temp
            E2+=Eb_temp
        else:
            E2+=Ea_temp
            E1+=Eb_temp
    
    E1_array = np.array(E1)
    kde = gaussian_kde(E1_array)
    e1_values = np.linspace(min(E1_array),max(E1_array),100)
    kde_E1 = kde(e1_values)
    
    E2_array = np.array(E2)
    kde = gaussian_kde(E2_array)
    e2_values = np.linspace(min(E2_array),max(E2_array),100)
    kde_E2 = kde(e2_values)
    
    kde_E1_n = (kde_E1-np.min(kde_E1))/(np.max(kde_E1)-np.min(kde_E1))
    kde_E2_n = (kde_E2-np.min(kde_E2))/(np.max(kde_E2)-np.min(kde_E2))
    
    plt.plot(e1_values,kde_E1_n)
    plt.plot(e2_values,kde_E2_n)
    plt.show()
        
        