# Mapreduce-BFS-
Contained is an advanced MapReduce program with python to implement BFS(Parallel Breadth-First Search) on a given input graph to determine the distance of each node 
from the source node. The code uses a graph.txt and distance.txt input files which inlcude an adjacency matrix of a graph and the distances of 
every node from the source (starts off as 9999 for every node but the source.)

### *Example graph.txt*:   
1: 2 3 4  
2: 5 6   
3: none   
4: 7 8   
5: 9 10   
6: none   
7: 3 11 12   
8: none   
9: none   
10: none   
11: none   
12: none   

### *Example distance.txt*:   
1: 0   
2: 9999   
3: 9999   
4: 9999  
5: 9999   
6: 9999    
7: 9999   
8: 9999   
9: 9999    
10: 9999   
11: 9999   
12: 9999    

# HOW TO RUN :  
Input files: graph.txt(mapper input), distance.txt 
output_filenames: mapreduce-outputX , X being iteration number  
e.g Final output = mapreduce-outputXmax , Xmax being the final iteration 

Source Code:  (no sub directories) 
 
    mapper.py
    reducer.py 
    reader.py
    run.sh



1. Remeber to delete or rename any /mapreduce-output file in the masternode working directory  

2. for each task after uploading the code and data to the cluster master node with the correct hadoop-streaming-3.1.4.jar file, make sure  
each run rile is runnable (chmod +x run.sh) and execute each run file in the cluster master node (./run.sh). 
