# Mapreduce-BFS-


# HOW TO RUN: 
Input files: graph.txt(mapper input), distance.txt
output_filenames: mapreduce-outputX , X being iteration number 
e.g Final output = mapreduce-outputXmax , Xmax being the final iteration

Source Code: all source code should be located in s3923076_BDP_A2 file (no sub directories)
 
    mapper.py
    reducer.py 
    reader.py
    run.sh



1. Remeber to delete or rename any /mapreduce-output file in the masternode working directory 

2. for each task after uploading the code and data to the cluster master node with the correct hadoop-streaming-3.1.4.jar file, make sure 
each run rile is runnable (chmod +x run.sh) and execute each run file in the cluster master node (./run.sh).
