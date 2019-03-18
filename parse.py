#!/usr/bin/python3
import math
from matrix import *
from display import * 
from draw import *

matrix = new_matrix()
'''Clears the edge matrix.'''
def clear():
    for i in matrix:
        for j in matrix[i]:
            matrix[i][j] = 0
'''Add a box to the edge matrix.'''
def box(x,y,z,width,height,depth):
    #width = How far into x
    #height = How far into y
    #depth = How far into z
    x1 = x + width
    y1 = y + height
    z1 = z + depth
    
    add_edge(ans,x,y,z,x1,y1,z1)
    
'''Add a sphere to the edge matrix.'''
def sphere(x,y,z,radius):
    pass
'''Add a torus into the edge matrix.'''
def torus(x,y,z,radius1,radius2):
    pass
