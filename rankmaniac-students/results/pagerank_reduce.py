#!/usr/bin/env python

import sys
import re

#
# This program simply represents the identity function.
#

node_pageranks = {}
prev_pageranks = {}
a = 0.85

for line in sys.stdin:

	# Now split by both tab and comma to account for pageranks having curr and prev vals	
	# arr = line.split('\t')
	arr = re.split('[\t,]',line)
	arr = list(map(float, arr))

	if arr[0] not in node_pageranks:
		node_pageranks[arr[0]] = []
		if (len(arr) == 3):
			prev_pageranks[arr[0]] = []

	node_pageranks[arr[0]].append(float(arr[1]))
	if (len(arr) == 3): # Retain the portions of the previous pr
		prev_pageranks[arr[0]].append(float(arr[2]))
	
n = len(list(node_pageranks.keys()))

for node_id, list_values in node_pageranks.items():
	# pageranks
	if node_id >= 0:
		page_rank = a*sum(list_values) + (1.-a)
		sys.stdout.write(str(node_id)+'\t'+ str(page_rank)+'\n')
	# iteration
	elif node_id == -1:
		sys.stdout.write(str(node_id)+'\t'+ str(sum(list_values))+'\n')
	# neighbors list
	else:
		prev_pagerank = sum(prev_pageranks[node_id])
		neighbor_string = ''
		for i, neighbor in enumerate(list_values):
			neighbor_string += str(int(neighbor))
			if i + 1 < len(list_values):
				neighbor_string += ','
		sys.stdout.write(str(node_id)+'\t' + str(prev_pagerank) + ',' + neighbor_string+'\n')





