#!/usr/bin/env python3

import sys

def getdistances(filepath):
    """Get distance.txt values (FORMAT: node# distance from source)
        get initial distances from a txt file and add them in an array
    """
    distances = {}
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if line:
                try:
                    line = line.strip()
                    dist = line.split(': ')
                    # dist[0] is node# and dist[1] is distance from source
                    distances['N'+dist[0]]=int(dist[1])
                except:
                    break
            else:
                break
            line = fp.readline()
    fp.close()

    return distances


# Input: graph.txt ( FORMAT = node: adjacentnode1 adjacentnode2 ect..)
def createpath(distances):
    """Inputs: graph.txt ( FORMAT = node: adjacentnode1 adjacentnode2 ect..)
        distances ( FORMAT = N(node #):distance from source)
    """
    for line in sys.stdin:
        Values = line.strip().split(':')
        Nodeid = Values[0]
        key ='N'+Nodeid
        # EMIT THE 2 value KEY <node id , N + nodeid >  
        print('%s,%s' % (Nodeid,key) ) 
        d = distances[key]
        print('%s,%s' % (Nodeid,str(d))) # emit value for current node
        children = Values[1].strip().split(' ')
        
        if children[0] != 'none':
            for node in children:
                Nodeid = node
                if d == 9999:
                    l=0
                else:
                    l=1
                # EMIT value of children of current node --> distance = distance of current node to source + 1 
                print('%s,%s' % (Nodeid,str(d+l)))# emit (m,d+l)
if __name__ == "__main__":
    distances = getdistances('distance.txt')
    createpath(distances)