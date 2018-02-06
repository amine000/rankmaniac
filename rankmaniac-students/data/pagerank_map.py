#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
	arr = line.split('\t')
	node_id = int(arr[0][7:])
	out_list = arr[1].split(',')[2:]
	out_list[-1] = out_list[-1][:-1]
	out_list = list(map(int, out_list))
	pageranks = list(map(float, arr[1].split(',')[:2]))
	degree = len(out_list)

	for neighbor in out_list:
		sys.stdout.write(str(neighbor)+'\t'+str(pageranks[0]/degree)+str('\n'))
		sys.stdout.write(str(node_id)+'\t'+str(0.)+'\n')
	
	if not out_list:
		sys.stdout.write(str(node_id)+'\t'+pageranks[0]+'\n')

