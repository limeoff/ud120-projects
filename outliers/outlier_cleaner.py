#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    i = 0
    for i in range(0, len(ages)):
        cleaned_data.append((float(ages[i]),float(net_worths[i]),float((net_worths[i]-predictions[i])**2)))

    print len(cleaned_data)

    cleaned_data.sort(key=lambda tup: tup[2])
    print cleaned_data
    cleaned_data = cleaned_data[0:int(len(cleaned_data) * .90)]

    print len(cleaned_data)
    print cleaned_data
    return cleaned_data

