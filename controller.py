#!/bin/env python
import csv
ga = __import__(args.genetic_algorithm)
ca = __import__(args.cluster_algorithm)

def readData(filename):
    data = [];
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|');
        rows = [];
        for row in reader:
        #    for col in row:
        #        rows.append(
        data.append(rows);

    return data;

def main():
    # Read in dataset from csv file
    data = readData(filename);
    
    k = 3;
    actK = 0;

    # Controller Constants
    phi = 1.0;
    pGain = 0.1;
    iGain = 0.0;
    dGain = 0.0;
    err = 0;
    dErr = 0;
    errLast = 0;
    sumErr = 0;
    errMax = 5;
    errMin = -2;

    # Genetic Algorithm Constants
    numTrials = 100;
    optima = [];

    # Generalized Crowding Constants
    #fitFunc;

    for i in range(1, 1000):
        # Proportional Term
        err = (k - actK);

        # Derivative Term
        dErr = err - errLast;
        errLast = err;

        # Integral Term
        sumErr += err;
        if (sumErr > errMax):
            sumErr = errMax;
        elif (sumErr < errMin):
            sumErr = errMin;

        phi = phi + pGain*err + iGain*sumErr + dGain*dErr;

        # Run Genetic Algorithm X times
        for j in range(1,numTrials):
            solution = ga.do_genetic_algorithm(phi, old_gen);
            optima.append(solution);

        # Run Generalized Crowding on solution set
        actK = ca.do_cluster_algorithm(k, optima, ff.do_fitness_function):

main();
