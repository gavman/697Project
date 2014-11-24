#!/bin/env python

import pandas as pd
import numpy as np
import random

#function do_cluster_algorithm
	#takes number of clusters as an input 1
	#takes generation of data as input 2
	#returns the clusters that get passed into the genetic algorithm
def do_cluster_algorithm(num_clusters, results, cluster_range):
  #results = create_kmean_data_frame(results)

  # run k-means with the desired number of clusters
  min_error = kmeans(results, num_clusters);
  print num_clusters, " error = ", min_error
  opt_clusters = num_clusters;

  # run k-means for range of number of clusters
  for i in xrange(1, cluster_range + 1):
    error = kmeans(results, num_clusters + i);
    print (num_clusters + i), " error = ", error
    if (error < min_error):
      min_error = error;
      opt_clusters = num_clusters + i;
    
    tmp_num = num_clusters - 1;
    if (tmp_num <= 0):
      pass;

    error = kmeans(results, num_clusters - i);
    print (num_clusters - i), " error = ", error
    if (error < min_error):
      min_error = error;
      opt_clusters = num_clusters - i;
    
  return opt_clusters

#function kmeans
    #takes the data as input 1
    #takes the number of means as input 2
#data is a data frame where each column is a vector of data at one data point
def kmeans(data, num_means):
    data.reset_index(drop=True, inplace=True)
    num_rows = len(data)
    maxes = data.max(axis = 1)
    mins = data.min(axis = 1)
        
    #means: each column is a n-dimensional mean
    #create random initial means
    means = pd.DataFrame(np.zeros((num_rows+1, num_means)))
    new_means = means.copy()
    for mean in xrange(num_means):
        new_means[mean].ix[num_rows] = 1
        for row in xrange(num_rows):
            min = int(round(mins.ix[row]))
            max = int(round(maxes.ix[row]))
            new_means[mean].ix[row] = float(random.randint(min, max))

    # Iterate until means do not change between iterations
    while (not means.equals(new_means)):
        # Copy means from last iteration and reset new means
        means = new_means.copy()
        new_means = pd.DataFrame(np.zeros((num_rows+1, num_means)))
        error = 0
        
        clusters = pd.Series(-1, np.arange(num_rows))
        # Find closest cluster for each data point
        for i in xrange(len(data.columns)):
            cluster_name = data.columns[i]
            cluster = data[cluster_name]
            shortest_dis = -1
            min_mean = 0
            for mean in means.columns:
                # Check for empty cluster
                if (means[mean].ix[num_rows] != 0):
                    dis = np.linalg.norm(cluster.sub(means[mean].ix[0:num_rows-1], axis=0))
                    if (shortest_dis == -1 or dis < shortest_dis):
                        shortest_dis = dis
                        min_mean = mean

            error += shortest_dis
            for row in xrange(len(maxes)):
                new_means[min_mean].ix[0:num_rows-1] += cluster
            new_means[mean].ix[num_rows] += 1

        # Compute new means for next iteration
        for mean in means.columns:
            if (new_means[mean].ix[num_rows] != 0):
                new_means[mean] = new_means[mean] / new_means[means].ix[num_rows]

    return error/len(data.columns)
