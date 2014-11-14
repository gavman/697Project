#!/bin/env python

import math

#function do_fitness_function in the file indicated by -ff flag
	#takes a data point as input 1. data_point is a tuple with an (x,y) point.
	#returns a fitness score
def do_fitness_function(data_point):
	x = data_point[0]
    y = data_point[1]
    return x*math.sin(math.sqrt(math.abs(x))) + y*math.sin(math.sqrt(math.abs(y))) + 2000
