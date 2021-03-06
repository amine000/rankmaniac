pagerank_map="pagerank_map.py"
pagerank_reduce="pagerank_reduce.py"
process_map="process_map.py"
process_reduce="process_reduce.py"
temp="temp.txt"
#!/bin/bash
for i in {1..5}
do
    echo “iteration $i done”;
    case $i in
    	1) 
			python $pagerank_map < input.txt | sort | python $pagerank_reduce | python $process_map | sort | python $process_reduce > 1temp.txt
			;;
		50)
			python $pagerank_map < $i$temp | sort | python $pagerank_reduce | python $process_map | sort | python $process_reduce > output.txt
			;;
		*)
			python $pagerank_map < $i$temp | sort | python $pagerank_reduce | python $process_map | sort | python $process_reduce > $((i+1))$temp
			;;
	esac
done