#!/bin/env python

import pandas as pd
import numpy as np
import string
import copy
from random import sample

#function do_genetic_algorithm
    #takes a scaling factor which is the exploration/exploitation trade-off
	#takes the current generation as input 2
	#returns a new generation of data
def do_genetic_algorithm(phi, old_gen):
    
    #load in the list of all words in all titles
    words = pd.Series.from_csv('data/all_words.csv')
    
    #how is the current list of words fairing?
    current_pct = naive_bayes(list(old_gen.values)
    #for each index, replace the word if the newly selected random word fares better
    for i in xrange(len(old_gen)):
        new_word = old_gen.values[0]
        # look for a new random word not already in our list
        while (new_word not in old_gen.values()):
            new_word = words.ix[np.array(sample(xrange(len(words)), 1))]
        
        #make a copy of our list, insert the new random word
        old_gen_copy = old_gen.copy()
        old_gen_copy[i] = new_word
        #how does the copy with the new word do in naive bayes?
        pct = naive_bayes(list(old_gen_copy))
        #if it fares better, use the new list of random words
        if (pct > current_pct):
            old_gen = old_gen_copy
            current_pct = pct

    #return the list remaining at the end
    return old_gen_copy


#words is a python list of key words
def naive_bayes(words):
    #topics
    topic_min = 1
    topic_max = 2

    #TODO split into training and testing
    data = pd.DataFrame.from_csv('data/titles_nice.csv')
    training_set = data
    testing_set = data


    priors = list()
    mu = pd.DataFrame([])
    sigma = pd.DataFrame([])

    total_count = training_set.Topic.count()
    for yk in xrange(topic_min, topic_max+1):
        this_data = data[data.Topic == yk]
        class_count = this_data.Topic.count()
        prior = float(class_count)/total_count
        priors.append(prior)

    #train
    word_probs = dict()
    for word in words:
        word_titles = training_set[training_set.Title.str.contains(word)]
        this_word_probs = list()
        for topic in xrange(topic_min, topic_max+1):
            word_count = float(word_titles[training_set.Topic == topic].Title.count())
            word_count_all = word_titles.Title.count()
            this_word_probs.append(word_count/word_count_all)
        word_probs[word] = this_word_probs

    #test
    num_correct = 0
    for i in xrange(testing_set.Title.count()):
        title = testing_set.Title.values[i]
        probs = copy.copy(priors)
        #multiply the priors by likelihood of topic given each word in our set
        for found_word in [word for word in words if word in title]:
            for topic in xrange(topic_min, topic_max+1):
                probs[topic-topic_min] *= word_probs.get(found_word)[topic-topic_min]
        #pick the topic with the greatest probability
        guess = probs.index(max(probs)) + topic_min
        if testing_set.Topic.values[i] == guess:
            num_correct += 1

    return float(num_correct)/testing_set.Title.count()
