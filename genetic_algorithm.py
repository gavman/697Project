#!/bin/env python

import pandas as pd
import numpy as np
import string

#function do_genetic_algorithm
    #takes a scaling factor which is the exploration/exploitation trade-off
	#takes the current generation as input 2
	#returns a new generation of data
def do_genetic_algorithm(phi, old_gen):
    return

#words is a list of words
def naive_bayes(words):
    #TODO split into training and testing
    data = pd.DataFrame.from_csv('titles_nice.csv')
    
    priors = list()
    mu = pd.DataFrame([])
    sigma = pd.DataFrame([])
    
    total_count = data.Topic.count()
    for yk in xrange(int(data.Topic.min(1), int(data.Topic.max(1)):
        this_data = data[data.Topic == yk]
        class_count = this_data.Topic.count()
        prior = float(class_count)/total_count
        priors.append(prior)
    
    #train
    titles = data.Titles()
    word_probs = list()
    for word in words:
        word_count = data[data.Title.str.contains(word)]
        word_count_one = float(word_count[data.Topic == 1].Title.count())
        word_count_two = float(word_count[data.Topic == 2].Title.count())
        word_count_all = word_count.Title.count()
        word_probs = (word_count_one/word_count_all, word_count_two/word_count_all)

    #TODO: test on testing set, return % correct
    #test
    for title in 
