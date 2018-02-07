#!/bin/bash
for i in {1..51}
do
echo “iteration $i done”;
   python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | python process_reduce.py
done