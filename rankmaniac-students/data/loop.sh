#!/bin/bash
<<<<<<< HEAD
<<<<<<< HEAD
for i in {1..41}
=======
for i in {1..1}
>>>>>>> def05ecd72438566bf31f567995f0352e2d74885
=======
for i in {1..5}
>>>>>>> bcf76a8b13f99b7ef7007b12f7a78280750c819f
do
echo “iteration $i done”;
   python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | python process_reduce.py > out.txt
done