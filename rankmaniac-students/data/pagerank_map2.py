#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
	arr = line.split('\t')
	node_id = int(arr[0][7:])
	info_list = arr[1].split(',')
	sink = (len(info_list) == 2)
	# no outgoing links, so there is just 1 in the diagonal of G
	if sink:
		sys.stdout.write(str(node_id)+'\t'+pageranks[0]+'\n')
	else:
		# otherwise count the contribution of this node to its neighbor's pageranks
		out_list = info_list[2:]
		out_list[-1] = out_list[-1][:-1]
		out_list = list(map(int, out_list))
		pageranks = list(map(float, arr[1].split(',')[:2]))
		degree = len(out_list)

		for neighbor in out_list:
			sys.stdout.write(str(neighbor)+'\t'+str(pageranks[0]/degree)+str('\n'))
			sys.stdout.write(str(node_id)+'\t'+str(0.)+'\n')