#!/bin/env python

import pandas as pd
import numpy as np
import random

#function do_cluster_algorithm
	#takes number of clusters as an input 1
	#takes generation of data as input 2
	#returns the clusters that get passed into the genetic algorithm
def do_cluster_algorithm(num_clusters, old_gen, fitness_function):
	return


#function distance_measure
	#takes a data point as input 1
	#takes a data point as input 2
	#returns the distance between input 1 and input 2
def distance_measure(data_val_one, data_val_two):
	return

#function kmeans
    #takes the data as input 1
    #takes the number of means as input 2
def kmeans(data, num_means):
    data.reset_index(drop=True, inplace=True)
    num_rows = len(data)
    maxes = data.max(axis = 1)
    mins = data.min(axis = 1)

    #create random initial means
    means = pd.DataFrame(np.zeros((num_rows, num_means)))
    for mean in xrange(num_means):
        for row in xrange(len(maxes)):
            min = int(round(mins.ix[row]))
            max = int(round(maxes.ix[row]))
            means[mean].ix[row] = float(random.randint(min, max))

    old_means = pd.DataFrame(np.zeros((num_rows, num_means)))
    #iterate
    while (not means.equals(old_means)):
        old_means = means.copy()
        clusters = pd.Series(-1, np.arange(num_rows))
        for cluster_name in data.columns:
            cluster = data[cluster_name]
            shortest_dis = -1
            for mean in means.columns:
                dis = np.linalg.norm(cluster.sub(means[mean], axis=0))
                if (shortest_dis == -1 or dis < shortest_dis):
                    shortest_dis = dis
                    clusters[cluster_name] = mean
        for mean in means.columns:
            num_columns = 0
            this_cluster = pd.DataFrame()
            for cluster in clusters:
                if cluster == mean:
                    this_cluster[num_columns] = data[cluster]
                    num_columns += 1
            means[mean] = this_cluster.mean(axis=1)
    
    #find total error
    error = 0.0
    for data_point in data.columns:
        mean = means[clusters[data_point]]
        error += np.linalg.norm(data[data_point].sub(mean, axis=0))

    return error
