pagerank_map="pagerank_map.py"
pagerank_reduce="pagerank_reduce.py"
process_map="process_map.py"
process_reduce="process_reduce.py"
temp="temp.txt"
#!/bin/bash
SECONDS=0
STARTTIME=`date +%s.%N`
for i in {1..16}
do
    echo “iteration $i done”;
    case $i in
    	1) 
			python $pagerank_map < input.txt | sort | python $pagerank_reduce | python $process_map | sort | python $process_reduce > 2temp.txt
			;;
		16)
			python $pagerank_map < $i$temp | sort | python $pagerank_reduce | python $process_map | sort | python $process_reduce > output.txt
			;;
		*)
			python $pagerank_map < $i$temp | sort | python $pagerank_reduce | python $process_map | sort | python $process_reduce > $((i+1))$temp
			;;
	esac
done

duration=$SECONDS
# do some work
ENDTIME=`date +%s.%N`
SEC1=`date +%s -d ${STARTTIME}`
SEC2=`date +%s -d ${ENDTIME}`
DIFFSEC=`expr ${SEC2} - ${SEC1}`
echo Took ${DIFFSEC} seconds.
echo "$(($ENDTIME-$STARTTIME))"

echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."