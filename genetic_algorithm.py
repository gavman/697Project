#!/bin/env python

import pandas as pd
import numpy as np
import string
import copy

#function do_genetic_algorithm
    #takes a scaling factor which is the exploration/exploitation trade-off
	#takes the current generation as input 2
	#returns a new generation of data
def do_genetic_algorithm(phi, old_gen):
    return

#test set of words for naive_bayes, has 80% accuracy
"""
words = list()
words.append('politics')
words.append('president')
words.append('gop')
words.append('democrat')
words.append('republicans')
words.append('war')
words.append('bush')
words.append('iraq')
"""


#words is a python list of key words
def naive_bayes(words):
    #topics
    topic_min = 1
    topic_max = 2

    #TODO split into training and testing
    data = pd.DataFrame.from_csv('titles_nice.csv')
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

print float(num_correct)/testing_set.Title.count()
