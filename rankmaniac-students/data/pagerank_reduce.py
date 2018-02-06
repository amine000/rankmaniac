#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

node_pageranks = {}
a = 0.85

for line in sys.stdin:
    arr = list(map(float, line.split('\t')))

    if arr[0] not in node_pageranks:
    	node_pageranks[arr[0]] = []

    node_pageranks[arr[0]].append(arr[1])
    
n = len(list(node_pageranks.keys()))

for node_id, list_values in node_pageranks.items():
	page_rank = a*sum(list_values) + (1.-a)
	sys.stdout.write(str(node_id)+'\t'+ str(page_rank)+'\n')

