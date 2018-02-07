#!/usr/bin/env python

import sys
#import os

#
# This program simply represents the identity function.
#

<<<<<<< HEAD
input_filename = 'input.txt'
input_filename2 = 'input2.txt'
MAX_ITER = 40
=======
#input_filename = '/Users/amineboubezari/rankmaniac/rankmaniac-students/data/input.txt'
#input_filename2 = '/Users/amineboubezari/rankmaniac/rankmaniac-students/data/input2.txt'
MAX_ITER = 2
>>>>>>> def05ecd72438566bf31f567995f0352e2d74885
node_list = []
node_dict = {}
node_neighbors = {}
iteration = 0

for line in sys.stdin:
	arr = line.split('\t')
	if int(arr[0]) == 1:
		node, pr = list(map(float, arr[1].split(',')))
		node_list.append([int(node), pr])
		node_dict[int(node)] = pr
	elif int(arr[0]) == 0:
		dummy_id, i = list(map(float, arr[1].split(',')))
		iteration = i
	else:
		info_arr = arr[1].split(',')
		n_node_id = int(-1*(float(info_arr[0]) + 2))
		neighbors = list(map(int, info_arr[1:]))
		node_neighbors[n_node_id] = neighbors

# done running, print final results
if iteration == MAX_ITER:	
	sorted_list = sorted(node_list, key=lambda val: -1*val[1])
	for val in sorted_list[:20]:
		node_id = int(val[0])
		pagerank = val[1]
		sys.stdout.write('FinalRank:'+str(pagerank)+'\t'+str(node_id)+'\n')
# not done, write output for next iteration
else:
	sys.stdout.write('$'+str(int(iteration)+1)+'\n')
	for node in node_list:
		node_id, pr = node
		write_string = 'NodeId:'+str(node_id)+'\t'+str(pr)+',0.0,'
		out_list = node_neighbors[node_id]
		for i, val in enumerate(out_list):
			write_string += str(val)
			if i + 1 < len(out_list):
				write_string += ','
		sys.stdout.write(write_string+'\n')
