from mapper import getdistances
#Checks to see if the current and previous distance files are the same (Termination condition)
def checkDistances(distance, distance1):
    same = True
    for key in distance:
        if distance[key] != distance1[key]: # Check each dictionary key value pair 
            same = False
    if same:
        print(1)
    else:
        print(0)
if __name__ == "__main__":
    # use getdistance func to import current and previous distance files as dictionaries 
    distance = getdistances('distance.txt')
    distance1 = getdistances('distance1.txt')
    
    checkDistances(distance, distance1)