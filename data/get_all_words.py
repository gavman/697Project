#/bin/env python

import pandas as pd
import string
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
"""
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

# get all the words that appear
all_words = set()
for title in titles.Title:
    for word in title.split(' '):
        all_words.add(word.lower())
word_series = pd.Series(list(all_words))
word_series.to_csv('all_words.csv')

#example set of words for naive bayes with 80% accuracy
words = list()
words.append('politics')
words.append('president')
words.append('gop')
words.append('democrat')
words.append('republicans')
words.append('war')
words.append('bush')
words.append('iraq')
words.append('in')
words.append('the')
words.append('presidential')
words.append('afghanistan')
words.append('terror')
first_gen = pd.Series(words)
first_gen.to_csv('first_gen.csv')
