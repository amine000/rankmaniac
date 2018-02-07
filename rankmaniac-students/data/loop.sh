#!/bin/bash
<<<<<<< HEAD
for i in {1..41}
=======
for i in {1..1}
>>>>>>> def05ecd72438566bf31f567995f0352e2d74885
do
echo “iteration $i done”;
   python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | python process_reduce.py
done