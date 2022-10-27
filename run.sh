#!/bin/bash
i=1
while :
do

	hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D mapred.reduce.tasks=1 \
    -D stream.map.output.field.separator="," \
    -D mapred.text.key.partitioner.options=-k1 \
    -file distance.txt \
    -file ./mapper.py \
    -mapper ./mapper.py \
    -file ./reducer.py \
    -reducer ./reducer.py \
    -input /graph.txt \
    -output /mapreduce-output$i \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
        
    rm -f distance1.txt
    hadoop fs -copyToLocal /mapreduce-output$i/part-00000 distance1.txt
    seeiftrue=`python reader.py` 
	
	if [ $seeiftrue = 1 ] 
	then # if current distance is the same as the previous distance file terminate loop and delete previous distance file 
		rm distance.txt
		hadoop fs -copyToLocal /mapreduce-output$i/part-00000 distance.txt
		break
	else # delete previous distance file and continue 
		rm distance.txt
		hadoop fs -copyToLocal /mapreduce-output$i/part-00000 distance.txt
	fi
	i=$((i+1))
done