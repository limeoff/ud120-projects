from sklearn.preprocessing import MinMaxScaler
import numpy
""" quiz materials for feature scaling clustering """

weights = numpy.array([[115.],[140.],[175.]])

scaler = MinMaxScaler()

rescaled_weight = scaler.fit_transform(weights)

print rescaled_weight


### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    arr2 = []

    #for a in arr:
    #    arr2.append((float(a)-min(arr))/(max(arr)-min(arr)))

    arr2 = [((float(a)-min(arr))/(max(arr)-min(arr))) for a in arr]

    return arr2


# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)