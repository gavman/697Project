#!/bin/env python

import argparse
parser = argparse.ArgumentParser(description='Framework for 18-697 project')
parser.add_argument('-ga', '--genetic-algorithm', help='location of the genetic algorithm function', required=True)
parser.add_argument('-ca', '--cluster-algorithm', help='location of the cluster algorithm function', required=True)
args = parser.parse_args()

import pandas as pd
import numpy as np
from random import sample

ga = __import__(args.genetic_algorithm)
ca = __import__(args.cluster_algorithm)

def main():
    k = 4
    actK = 0

    # Generating new word sets
    training_set = pd.DataFrame.from_csv('data/training_set.csv')
    testing_set = pd.DataFrame.from_csv('data/testing_set.csv')
    all_words = pd.Series.from_csv('data/all_words.csv')
    num_sets = 5
    words_per_set = 10

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
    cluster_range = 2

    # Genetic Algorithm Constants
    numTrials = 25
    optima = pd.DataFrame();

    # Generalized Crowding Constants
    #fitFunc;

    for i in xrange(50):
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

        new_gen = pd.DataFrame()
        scores = pd.DataFrame()
        # Run Genetic Algorithm X times
        for j in xrange(numTrials):
            data = generate_new_random_word_sets(num_sets, words_per_set, all_words)
            (new_gen_vector, scoring) = ga.do_genetic_algorithm(phi, data)
            scores[len(scores.columns)] = scoring[1]
            new_gen[len(new_gen.columns)] = new_gen_vector

        # Run Generalized Crowding on solution set
        actK = ca.do_cluster_algorithm(k, scores, cluster_range)

        new_gen.to_csv('gens/new_gen_' + str(i) + '.csv')

        # Calculate
        (pct,result) = ga.naive_bayes_total(new_gen, training_set, testing_set)
        print "Combined accuracy:", pct

def generate_new_random_word_sets(num_sets, words_per_set, all_words):
    word_sets = pd.DataFrame()
    for i in xrange(num_sets):
        sample_indexes = sample(xrange(len(all_words)), words_per_set)
        word_sets[len(word_sets.columns)] = all_words[sample_indexes].reset_index(drop=True)
    return word_sets

if __name__ == '__main__':
    main()
