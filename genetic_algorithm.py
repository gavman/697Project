#!/bin/env python

import pandas as pd
import numpy as np
import string
import copy
import random

def do_genetic_algorithm(phi, sets):
    
    #some file io to pass around
    training_set = pd.DataFrame.from_csv('data/training_set.csv')
    testing_set = pd.DataFrame.from_csv('data/testing_set.csv')
    all_words = pd.Series.from_csv('data/all_words.csv')

    while(len(sets.columns) > 1):
        pcts = list()
        results = list()
        for column in sets.columns:
            this_set = sets[column]
            (pct, result) = naive_bayes(this_set, training_set, testing_set)
            pcts.append(pct)
            results.append(result)

        #find smallest index of two smallest pcts
        min_index = pcts.index(min(pcts))
        pcts[min_index] = max(pcts)
        min_index_two = pcts.index(min(pcts))
        to_delete = min_index
        if (phi > 0 and random.random() > .5):
            to_delete = min_index_two
        
        del sets[sets.columns[to_delete]]

        #mutate each set
        for column in sets.columns:
            this_set = sets[column]
            new_set = mutate(this_set, all_words, training_set, testing_set)
            sets[column] = new_set
    
    #return the one column
    to_return = sets[sets.columns[0]]
    return to_return, naive_bayes(to_return, training_set, testing_set)[1]

#function mutate
    #takes a scaling factor which is the exploration/exploitation trade-off
	#takes the current generation as input 2
	#returns a new generation of data
def mutate(old_gen, all_words, training_set, testing_set):
    
    #for each index, replace the word if the newly selected random word fares better
    for i in xrange(len(old_gen)):
        new_word = old_gen.values[0]
        # look for a new random word not already in our list
        while (new_word not in old_gen.values):
            new_word = words.ix[np.array(sample(xrange(len(words)), 1))]
        
        #make a copy of our list, insert the new random word
        old_gen_copy = old_gen.copy()
        old_gen_copy[i] = new_word
        #how does the copy with the new word do in naive bayes?
        #if it fares better, use the new list of random words
        if (random.random() > .75):
            old_gen = old_gen_copy

    #return the list remaining at the end
    return old_gen


#words is a python list of key words
def naive_bayes(words, training_set, testing_set):
    #topics
    topic_min = 1
    topic_max = 2
    
    priors = list()
    total_count = training_set.Topic.count()
    for yk in xrange(topic_min, topic_max+1):
        this_data = training_set[training_set.Topic == yk]
        class_count = this_data.Topic.count()
        prior = float(class_count)/total_count
        priors.append(prior)

    #train
    word_probs = dict() #maps word to list of probs for each topic
    for word in words:
        word_titles = training_set[training_set.Title.str.contains(word)]
        this_word_probs = list()
        word_count_all = word_titles.Title.count()
        for topic in xrange(topic_min, topic_max+1):
            word_count = float(word_titles[training_set.Topic == topic].Title.count())
            if (word_count_all != 0):
                this_word_probs.append(word_count/word_count_all)
            else:
                #word never appreas in any topic, 1 for no change to prob
                this_word_probs.append(1.0)
        word_probs[word] = this_word_probs

    #test
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in xrange(testing_set.Title.count()):
        title = testing_set.Title.values[i]
        probs = copy.copy(priors)
        #multiply the priors by likelihood of topic given each word in our set
        for found_word in [word for word in words if word in title]:
            for topic in xrange(topic_min, topic_max+1):
                probs[topic-topic_min] *= word_probs.get(found_word)[topic-topic_min]
        #pick the topic with the greatest probability
        guess = probs.index(max(probs)) + topic_min
        actual_answer = training_set.Topic.values[i]
        if guess == 1 and actual_answer == 1:
            tp += 1
        elif guess == 1 and actual_answer == 2:
            fp += 1
        elif guess == 2 and actual_answer == 2:
            tn += 1
        else:
            fn += 1
    results = list()
    results.append(tp)
    results.append(fp)
    results.append(tn)
    results.append(fn)
    return (float(tp+tn)/testing_set.Title.count(), pd.Series(results))
