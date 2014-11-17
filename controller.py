#!/bin/env python

import argparse
parser = argparse.ArgumentParser(description='Framework for 18-697 project')
parser.add_argument('-ga', '--genetic-algorithm', help='location of the genetic algorithm function', required=True)
parser.add_argument('-ca', '--cluster-agorithm', help='location of the cluster algorithm function', required=True)
args = parser.parse_args()

import pandas
ga = __import__(args.genetic_algorithm)
ca = __import__(args.cluster_algorithm)

def main():
    # Read in dataset from csv file
    data = pd.Series.from_csv('data/first_gen.csv');
    
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

    #cluster range
    cluster_range = 5

    # Genetic Algorithm Constants
    numTrials = 100
    optima = pd.DataFrame();

    # Generalized Crowding Constants
    #fitFunc;

    for i in range(1, 1000):
        # Proportional Term
        err = (k - actK)

        # Derivative Term
        dErr = err - errLast
        errLast = err

        # Integral Term
        sumErr += err;
        if (sumErr > errMax):
            sumErr = errMax
        elif (sumErr < errMin):
            sumErr = errMin

        phi = phi + pGain*err + iGain*sumErr + dGain*dErr

        # Run Genetic Algorithm X times
        for j in range(1,numTrials):
            solution = ga.do_genetic_algorithm(phi, old_gen)
            optima[len(optima.columns)] = solution

        # Run Generalized Crowding on solution set
        actK = ca.do_cluster_algorithm(k, optima, cluster_range)

if __name__ == '__main__':
    main()
