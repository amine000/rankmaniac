#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
	# not on first iteration
	if line[0] == '$':
		sys.stdout.write(str(-1)+'\t'+line[1:-1].split('\t')[0]+'\n')
		continue
	else:
		pass
		#sys.stdout.write(str(-1)+'\t'+str(0)+'\n')

	arr = line.split('\t')
	node_id = int(arr[0][7:])
	n_node_id = -1*node_id - 2
	info_list = arr[1].split(',')
	sink = (len(info_list) == 2)
	pageranks = list(map(float, arr[1].split(',')[:2]))

	# no outgoing links, so there is just 1 in the diagonal of G
	if sink:
		pass
		#sys.stdout.write(str(node_id)+'\t'+str(pageranks[0])+'\n')
	else:
		# otherwise count the contribution of this node to its neighbor's pageranks
		out_list = info_list[2:]
		out_list[-1] = out_list[-1][:-1]
		out_list = list(map(int, out_list))
		degree = len(out_list)
		#sys.stdout.write(str(node_id)+'\t'+str(0.)+'\n')

		for neighbor in out_list:
			sys.stdout.write(str(neighbor)+'\t'+str(pageranks[0]/degree)+'\n')
			sys.stdout.write(str(n_node_id)+'\t'+str(neighbor)+'\n')
