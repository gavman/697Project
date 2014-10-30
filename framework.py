#!/bin/env python

#requires 3 functions in 3 other files:

#function do_cluster_algorithm in file indicated by -ca flag
	#takes number of clusters as an input 1
	#takes generation of data as input 2
	#returns the clusters that get passed into the genetic algorithm

#function do_genetic_algorithm in file indicated by -ga flag
	#takes clusters returned from do_cluster_algorithm as input 1
	#takes a generation of data as input 2
	#returns a new generation of data

#function do_fitness_function in the file indicated by -ff flag
	#takes a data point as input 1
	#returns a fitness score

#parse command line argument
import argparse
parser = argparse.ArgumentParser(description="Run and cluster a genetic algorithm on a fitness function")
parser.add_argument('-k' , '--num-clusters', help='number of clusters', required=True)
parser.add_argument('-ga', '--genetic-algorithm', help='location of genetic algorithm', required=True)
parser.add_argument('-ca', '--cluster-algorithm', help='location of cluster algorithm', required=True)
parser.add_argument('-ff', '--fitness-function', help='location of fitness function', required=True)
args = parser.parse_args()

ga = __import__(args.genetic_algorithm)
ca = __import__(args.cluster_algorithm)
ff = __import__(args.fitness_function)
num_clusters = args.num_clusters

old_gen = 1 # initial data
new_gen = None

# main algorithm
# first cluser the generation we have
# then pick which clusters to keep based on the fitness function
# then create a new generation from the kept clusters
# stop when there is no improvement from the old gen to the new gen
while(new_gen better than old_gen):
	clusters = ca.do_cluster_algorithm(num_clusters, old_gen, ff.do_fitness_function)
	new_gen = ga.do_genetic_algorithm(clusters, ff.do_fitness_function)
