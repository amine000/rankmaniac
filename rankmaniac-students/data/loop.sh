#!/bin/bash
OUTPUT = “$(python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py)”;
for i in {1..1}
do
echo “iteration $i done”;
OUTPUT = “$(python pagerank_map.py <<< $OUTPUT | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py)”;
done