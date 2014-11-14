#!/bin/env python

#parse command line argument
import argparse
parser = argparse.ArgumentParser(description="Run and cluster a genetic algorithm based on a fitness function")
parser.add_argument('-k' , '--num-clusters',      help='number of clusters',                                  required=True)
parser.add_argument('-ga', '--genetic-algorithm', help='location of file with do_genetic_algorithm function', required=True)
parser.add_argument('-ca', '--cluster-algorithm', help='location of file with do_cluster_algorithm function', required=True)
parser.add_argument('-ff', '--fitness-function',  help='location of file with do_fitness_function function',  required=True)
parser.add_argument('-df', '--data-file',         help='csv file with dataset',                               required=True)
args = parser.parse_args()

ga = __import__(args.genetic_algorithm)
ca = __import__(args.cluster_algorithm)
ff = __import__(args.fitness_function)

import csv

def readData(filename):
    data = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rows = []
        for row in reader:
        #    for col in row:
        #        rows.append(
        data.append(rows)

    return data;

def main():
    # Read in dataset from csv file
    data = readData(args.data_file);
    
    k = 3
    actK = 0

    # Controller Constants
    phi = 1.0
    pGain = 0.1
    iGain = 0.0
    dGain = 0.0
    err = 0
    dErr = 0
    errLast = 0
    sumErr = 0
    errMax = 5
    errMin = -2

    # Genetic Algorithm Constants
    numTrials = 100
    optima = []

    # Generalized Crowding Constants
    #fitFunc;

    for i in range(1, 1000):
        # Proportional Term
        err = (k - actK)

        # Derivative Term
        dErr = err - errLast
        errLast = err

        # Integral Term
        sumErr += err
        if (sumErr > errMax):
            sumErr = errMax
        elif (sumErr < errMin):
            sumErr = errMin

        phi = phi + pGain*err + iGain*sumErr + dGain*dErr

        # Run Genetic Algorithm X times
        for j in range(1,numTrials):
            solution = ga.do_genetic_algorithm(phi, ff.do_fitness_function, old_gen)
            optima.append(solution)

        # Run Generalized Crowding on solution set
        actK = ca.do_cluster_algorithm(k, optima, ff.do_fitness_function)

if __name__ == "__main__":
    main();
