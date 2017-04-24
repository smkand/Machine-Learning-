
#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

import re

import numpy as np

enron_data = pickle.load(open("/Users/shobhaMkand/Desktop/myml/final_project/final_project_dataset.pkl", "r"))


print "Data points", len(enron_data)

print "No of features", len(enron_data[enron_data.keys()[0]])  

poi_dataset = 0

for name,features in enron_data.iteritems():
    if features['poi']:
        poi_dataset += 1
    print "POI in dataset:", poi_dataset
    
poi_all = 0

with open("/Users/shobhaMkand/Desktop/myml/final_project/poi_names.txt") as f:
    content = f.readlines()
for line in content:  
    if re.match( r'\((y|n)\)', line):
        poi_all += 1
        
print "All POI:", poi_all + 10

print "Stock value of James Prentice:", enron_data["PRENTICE JAMES"]['total_stock_value']
print "Email messages from Wesley Colwell:", enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
print "Stock options exercised by Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]['exercised_stock_options']


print "Total payment by Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]['total_payments']
print "Total payment by Kenneth Lay:", enron_data["LAY KENNETH L"]['total_payments']
print "Total payment by Andrew Fastow:", enron_data["FASTOW ANDREW S"]['total_payments']



salaries_available = 0
emails_available = 0
total_payments_unavailable = 0
total_payments_unavailable_poi = 0
for name in enron_data:
    if not np.isnan(float(enron_data[name]['salary'])):
        salaries_available += 1
    if enron_data[name]['email_address'] != "NaN":
        emails_available += 1
    if np.isnan(float(enron_data[name]['total_payments'])):
        total_payments_unavailable += 1
        if enron_data[name]['poi']:
            total_payments_unavailable_poi += 1
        
    
print "Salaries available:", salaries_available
print "Emails available:", emails_available
print "NaN for total payment and percentage:", total_payments_unavailable, float(total_payments_unavailable)/len(enron_data)*100
print "NaN for total payment of POI and percentage:", total_payments_unavailable_poi, float(total_payments_unavailable_poi)/poi_dataset*100



print "Features:", enron_data[enron_data.keys()[0]]

print "Number of people +10 =", len(enron_data)+10

print "Number with NaN for total payments +10 =", sum(1 for person in enron_data.values() if person['total_payments'] == 'NaN')+10


