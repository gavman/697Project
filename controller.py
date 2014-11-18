#!/bin/env python

import argparse
parser = argparse.ArgumentParser(description='Framework for 18-697 project')
parser.add_argument('-ga', '--genetic-algorithm', help='location of the genetic algorithm function', required=True)
parser.add_argument('-ca', '--cluster-algorithm', help='location of the cluster algorithm function', required=True)
args = parser.parse_args()

import pandas as pd
ga = __import__(args.genetic_algorithm)
ca = __import__(args.cluster_algorithm)

def main():
    # Read in dataset from csv file
    data = pd.Series.from_csv('data/first_gen.csv');
    
    k = 2
    actK = 0

    # Controller Constants
    phi = 1.0
    pGain = 0.1
    iGain = 0.0
    dGain = 0.0
    err = 0
    dErr = 0
    errLast = -1
    sumErr = 0
    errMax = 5
    errMin = -2

    #cluster range
    cluster_range = 1

    # Genetic Algorithm Constants
    numTrials = 4
    optima = pd.DataFrame();

    # Generalized Crowding Constants
    #fitFunc;

    for i in xrange(15):
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
        print "phi = ", phi

        # Run Genetic Algorithm X times
        for j in xrange(numTrials):
            solution = ga.do_genetic_algorithm(phi, data)
            optima[len(optima.columns)] = solution

        # Run Generalized Crowding on solution set
        actK = ca.do_cluster_algorithm(k, optima, cluster_range)

if __name__ == '__main__':
    main()
