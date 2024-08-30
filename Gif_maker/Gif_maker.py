#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:49:30 2024

@author: pdam-linux
Gift maker for montecarlo class
"""

# importing usefull libraries
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
import imageio
import os

# Global vars
# x_space = np.linspace(0,1,100)
# y_space = np.linspace(0,1,100)


def cheker (func,x,y):
    """
    This funct takes a lambda, or normal function that has to return float
    and returns bulean True or False if the pair x,y below the function
    """
    return y <= func(x)

#Frame maker

def create_frame_in_out (sctr_in,sctr_out,file_name):
    """
    Creates a frame
    """
    global x_space, y_space
    plt.figure()
    plt.plot(x_space,y_space)
    plt.scatter(sctr_in[0], sctr_in[1])
    plt.scatter(sctr_out[0],sctr_out[1])
    plt.savefig(file_name)
    plt.close()
    
def Make_in_out_Gif (x_points,y_points,func):
    """
    this makes the gif
    """
    output_dir = 'temp_images'
    os.makedirs(output_dir, exist_ok=True)
    filenames = []
    
    x_min = np.min(x_points)
    x_max = np.max(x_points)
    
    global x_space, y_space
    x_space = np.linspace(x_min,x_max,100)
    y_space = func(x_space)
    
    in_points = [[],[]]
    out_points = [[],[]]
    
    frame_i = 0
    for xr,yr in zip(x_points,y_points):
        if cheker(func, xr, yr):
            in_points[0].append(xr)
            in_points[1].append(yr)
        else:
            out_points[0].append(xr)
            out_points[1].append(yr)
        file_name = os.path.join(output_dir, f'frame_{frame_i:.2f}.png')
        create_frame_in_out(in_points, out_points, file_name)
        frame_i += 1
        filenames.append(file_name)
    
    with imageio.get_writer('anmiation.gif', mode='I', duration = 0.1) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
            
    for filename in filenames:
        os.remove(filename)
    


if __name__ == '__main__':
    
    #lets plot the integrand
    x = np.linspace(0,1.25,100)
    y = (2/np.sqrt(np.pi))*np.exp(-x**2)
    
    # Solve it by Hit and miss
    Z = 1.25
    y_max = 2/np.sqrt(np.pi)
    # N number of points
    N = 100
    # generating random values
    x_r = rand(N)*Z
    y_r = rand(N)*y_max
    
    # This logic finds the hits and store them
    hits = y_r <= y_max*np.exp(-x_r**2)
    
    # Fraction of hits
    f = np.sum(hits)/N
    area = f*(Z*y_max)
    print(area)
    
    erf_z = lambda z : (2/np.sqrt(np.pi))*np.exp(-z**2)

    Make_in_out_Gif(x_r, y_r, erf_z)
    
    