#!/usr/bin/env python

import sys

def calculateNewDistances():
    d_min = {}
    distance = {}
    M=None
   
    for line in sys.stdin:
        # these IF statements only work because Hadoop sorts map output
        # by key before it is passed to the reducer. Therefore all the calculate <nodeid,distance> pairs for a 
        # specific nodeid will be parsed first 
        

        Nodeid,d = line.split('\t')
        if Nodeid not in d_min.keys():
            d_min[Nodeid] = 9999
        
        if d[0]=='N':  # checks for key  (<nodeid,N+nodeid>)
            M = d
            
        else:
            try:
                d = int(d)
                # finds the current minimum distance from source of current node 
                if d < d_min[Nodeid]:
                    d_min[Nodeid] = d
            except ValueError:
                # float was not a number, so silently
                # ignore/discard this line
                continue
        distance['N'+Nodeid]=d_min[Nodeid] # set distance value for current node to minimum distance 
    for key in distance: # Print all distances in the distance dictionary containing all minimum distances 
        print('%s: %s' % (key[1:],str(distance[key])))
    
        
        
           
if __name__ == "__main__":
    calculateNewDistances()