#!/bin/bash
for i in {1..3}
do
echo “iteration $i done”;
   python pagerank_map.py < outgnp.txt | sort | python pagerank_reduce.py | python process_map.py | python process_reduce.py > outgnp2.txt
done