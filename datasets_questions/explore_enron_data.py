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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
#print list(enron_data.keys())
print len(enron_data["SKILLING JEFFREY K"])
print enron_data["SKILLING JEFFREY K"]

count_poi = 0
for k, v in enron_data.items():
    #sum(1 for i in v.["poi"] if i == true)
    if v["poi"] == True:
        count_poi += 1
print count_poi

print sum(enron_data[key]['poi'] for key in enron_data)

poi_file = open("../final_project/poi_names.txt", 'r')
#poi_list = [line.split('(') for line in poi_file.readlines()]
poi_list = poi_file.read().split('\n')
poi_file.close()
poi_names = [name for name in poi_list if "(y)" in name or "(n)" in name]
print len(poi_names)
#print poi_list

#Quiz: Query The Dataset 2
name = "Colwell Wesley"
print enron_data[name.upper()]["from_this_person_to_poi"]
print name.upper()
#Quiz: Query The Dataset 3
name = "SKILLING JEFFREY K"
print enron_data[name.upper()]["exercised_stock_options"]

#Quiz: Follow The Money

mykeys = ["SKILLING JEFFREY K","LAY KENNETH L","FASTOW ANDREW S"]

for k, v in enron_data.iteritems():
    if k in mykeys: print k, "=>", v["total_payments"]

#Quiz: Dealing With Unfilled Features
have_salary = 0
have_email_address = 0
for k, v in enron_data.iteritems():
    if v["salary"] != "NaN": have_salary += 1
    if v["email_address"] != "NaN": have_email_address += 1
print have_salary, have_email_address

#Quiz: Missing POIs 1 (Optional)
not_have_total_payments = 0
for k, v in enron_data.iteritems():
    if v["total_payments"] == "NaN": not_have_total_payments += 1

total_poi = len(enron_data)*count_poi
print "People who not have total payments:", float(not_have_total_payments)/len(enron_data)*100

print "People who not have total payments(from whole poi):", float(not_have_total_payments)/21*100

# What percentage of POIs in the data have "NaN" for their total payments?
POIs = dict((key,value) for key, value in enron_data.iteritems() if value['poi'] == True)
number_POIs = len(POIs)
no_total_payments = len(dict((key, value) for key, value in POIs.items() if value["total_payments"] == 'NaN'))
print float(no_total_payments)/number_POIs * 100

#Quiz: Missing POIs 4 (Optional)
print not_have_total_payments+10, len(enron_data)+10

#Quiz: Missing POIs 5 (Optional)
#What is the new number of POIs in the dataset?
#What is the new number of POIs with NaN for total_payments?

print number_POIs+10, 