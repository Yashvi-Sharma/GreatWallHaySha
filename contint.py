import numpy as np 


def distances(p1,p2):
    
    # fill this in 
    
    return np.sqrt((p2[0]-p1[0])**2 + (p2[1] - p1[1])**2)

def average(distances):
    
    # fill this in 
    distances = np.atleast_1d(distances)
    avg = np.sum(distances)/len(distances)
    return avg
