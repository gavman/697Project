#!/bin/env python

#function do_cluster_algorithm
	#takes number of clusters as an input 1
	#takes generation of data as input 2
	#returns the clusters that get passed into the genetic algorithm
def do_cluster_algorithm(num_clusters, results, cluster_range):
  # run k-means with the desired number of clusters
  min_error = kMeans(results, num_clusters);
  min_clusters = num_clusters;

  # run
  for i in range(1, cluster_range):
    fitness = kMeans(results, num_clusters + i);
    
    tmp_num = num_clusters - 1;
    if (tmp_num <= 0):
      continue;
    fitness = kMeans(results, num_clusters - i);
    
  return


#function distance_measure
	#takes a data point as input 1
	#takes a data point as input 2
	#returns the distance between input 1 and input 2
def distance_measure(data_val_one, data_val_two):
  return
