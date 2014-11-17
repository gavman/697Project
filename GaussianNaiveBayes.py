#!/bin/env python

#parse command line arguments
import argparse
parser = argparse.ArgumentParser(description="A gaussian naive bayes program")
parser.add_argument('-trd', '--training-data', help='location of training data', required=True)
parser.add_argument('-ted', '--testing-data', help='location of testing data', required=True)
parser.add_argument('-nf', '--num-features', help='number of features', type=int, required=True)
args = parser.parse_args()

import math
import pandas as pd

def train():
    all_lines = list()
    #parse the data from the file
    f = open(args.training_data)
    for line in f:
        line_list = parse_line(line)
        all_lines.append(line_list)
    f.close()
    #put all data in a pandas data frame, get min and max class #1
    data = pd.DataFrame(all_lines)
    ymin = int(data[args.num_features].min(1))
    ymax = int(data[args.num_features].max(1))

    priors = list()
    mu = pd.DataFrame([])
    sigma = pd.DataFrame([])
    #compute prior probabilities of each class 
    for yk in xrange(ymin, ymax+1):
        #grab data with correct class
        this_data = data[data[args.num_features] == yk]

        class_count = this_data.count()[0]
        total_count = data.count()[0]
        prior = float(class_count)/total_count
        print "Class", yk, "is found", class_count, "times out of", total_count, "records"
        print "The prior probablilty of class", yk, "=", prior
        priors.append(prior)
   
        #append to mu and sigma
        mu = mu.append(pd.DataFrame(this_data.mean(0)).transpose())
        sigma = sigma.append(pd.DataFrame(this_data.var(0)).transpose())
    
    #reformat and print mu and sigma
    del mu[args.num_features]
    del sigma[args.num_features]
    mu.reset_index(inplace=True, drop=True)
    sigma.reset_index(inplace=True, drop=True)
    print "mu:\n", mu
    print "sigma:\n", sigma
    return (mu, sigma, ymin, ymax)    

def test(mu, sigma, ymin, ymax):
    f = open(args.testing_data)
    #classify line by line
    total_classified = 0
    correctly_classified = 0
    for line in f:
        line_list = parse_line(line)
        #store the max_probability and the classification for this line
        max_prob = 0.
        classification = 0
        #calculate probability for each class
        for yk in xrange(0, ymax-ymin+1):
            product = 1.
            #multiply together probability of each feature
            for i in xrange(args.num_features):
                p = gaussian(mu[i].ix[yk], sigma[i].ix[yk], line_list[i])
                product *= p
            #check if this product is the new max
            if product > max_prob:
                max_prob = product
                classification = yk + ymin
        print "line was classified as", classification, "and was supposed to be classified as", int(line_list[args.num_features])
        
        if classification == int(line_list[args.num_features]): correctly_classified += 1
        total_classified += 1

    print correctly_classified, "out out", total_classified, "lines were correctly classified"
    print "Accuracy:", 100*float(correctly_classified)/total_classified, "%"
    f.close()
    return

#parse a line of the .txt files
def parse_line(line):
    line_list = line.split(" ")
    line_list = filter(lambda x: x != "", line_list)
    line_list[-1] = line_list[-1].strip()
    line_list = map(lambda x: float(x), line_list)
    return line_list

#return P(x) for a gaussian PDF with mean mu and variance sigma
def gaussian(mu, sigma, x):
    c = 1./math.sqrt(2*math.pi*sigma)
    exp = math.exp(-.5*(((x-mu)**2)/(sigma)))
    return c*exp

def main():
    (mu, sigma, ymin, ymax) = train()
    test(mu, sigma, ymin, ymax)

if __name__ == "__main__":
    main()
