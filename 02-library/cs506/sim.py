import math
import numpy as np

# returns magnitude of a passed array
def magnitude(x):
    rhet = 0

    for val in x:
        rhet += val **2

    return math.sqrt(rhet)

def euclidean_dist(x, y):
    
    total = 0

    # Choose the smaller array to iterate over
    smallerArr = x
    if len(x) > len(y):
        smallerArr = y

    for i in range(len(smallerArr)):
        total += (x[i] - y[i]) ** 2

    return math.sqrt(total)

def manhattan_dist(x, y):

    total = 0

    # Choose the smaller array to iterate over
    smallerArr = x
    if len(x) > len(y):
        smallerArr = y

    for i in range(len(smallerArr)):
        total += abs(x[i] - y[i])

    return total

def jaccard_dist(x, y):
    
    setX = set(x)
    setY = set(y)

    unionLen = len(setX.union(setY))
    interLen = len(setX.intersection(setY))

    if(unionLen != 0):
        return (unionLen - interLen) / unionLen
    else:
        return float('inf')

def cosine_sim(x, y):

    if(len(x) != len(y)):
        return 'Vectors not of same size, cannot find cosine similarity.'
    
    dotProduct = np.dot(x, y)

    magnitudeProduct = magnitude(x) * magnitude(y)

    if(magnitudeProduct != 0):
        return dotProduct/magnitudeProduct
    else:
        return float('inf')

# Feel free to add more
