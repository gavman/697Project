import pandas as pd

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

"""
for i in xrange(10):
    this_data = data[data['Topic'] == i+1]
    print i+1, len(this_data) 
"""
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
