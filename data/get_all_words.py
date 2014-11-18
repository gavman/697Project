#/bin/env python

import pandas as pd
import numpy as np
import string
from random import sample
"""
#filter the data
data = pd.DataFrame.from_csv('data.csv')
data = data[[
    'Title', 
    'War on Terror', 
    'Katrina', 
    'Israel/Palestine', 
    'Immigration', 
    'Presidential Elections', 
    'Clinton Impeachment', 
    'Enron', 
    'Darfur', 
    'Race/Ethnicity', 
    'Schiavo']]

data['Topic'] = data['War on Terror'] * 1 + \
                data['Katrina'] * 2 + \
                data['Israel/Palestine'] * 3 + \
                data['Immigration'] * 4 + \
                data['Presidential Elections'] * 5 + \
                data['Clinton Impeachment'] * 6 + \
                data['Enron'] * 7 + \
                data['Darfur'] * 8 + \
                data['Race/Ethnicity'] * 9 + \
                data['Schiavo'] * 10

data = data[['Title', 'Topic']]
data = data[data['Topic'] > 0].reset_index(drop=True)


#for i in xrange(10):
#    this_data = data[data['Topic'] == i+1]
#    print i+1, len(this_data) 

# We see the number of articles per topic is:
# War on Terror: 4170
# Katrina: 162
# Israel/Palestine: 1057
# Immigration: 359
# Presidential Elections: 1597
# Clinton Impeachment: 477
# Enron: 183
# Darfur: 26
# Race/Ethnicity: 437
# Schiavo: 27

data = data.query('Topic == 5').append(data.query('Topic == 1'))
data.Topic = data.Topic.replace('5', '2')

data.reset_index(drop=True, inplace=True)

pd.DataFrame.to_csv(data, 'data_filtered.csv')

# make the titles nice
exclude = set(string.punctuation)
exclude.add('\n')
new_titles = pd.Series([])
titles = pd.DataFrame.from_csv('data_filtered.csv')
for title in titles.Title:
    title = "".join(ch for ch in title if ch not in exclude)
    new_titles = new_titles.append(pd.Series([title.lower()]))

titles['Title'] = new_titles.values
titles.to_csv('titles_nice.csv')
"""


#get data
data = pd.DataFrame.from_csv('titles_nice.csv')
#split into training and testing sets
training_pct = .7
num_training_indexes = int(training_pct*len(data))
sampled_indexes = sample(xrange(len(data)), num_training_indexes)
other_indexes = [x for x in xrange(len(data)) if x not in sampled_indexes]
training_set = data.ix[np.array(sampled_indexes)]
testing_set = data.ix[np.array(other_indexes)]

training_set.to_csv('training_set.csv')
testing_set.to_csv('testing_set.csv')

all_words = set()
for title in training_set.Title:
    for word in title.split(' '):
        all_words.add(word.lower())
word_series = pd.Series(list(all_words))
word_series.to_csv('all_words.csv')
