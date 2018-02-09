#!/usr/bin/env python

import sys
#import os

#
# This program simply represents the identity function.
#

def print_final_nodes(node_list):
	sorted_list = sorted(node_list, key=lambda val: -1*val[1])
	for val in sorted_list[:20]:
		node_id = int(val[0])
		pagerank = val[1]
		sys.stdout.write('FinalRank:'+str(pagerank)+'\t'+str(node_id)+'\n')

def calculate_residuals(node_list, previous_pageranks):
	residuals = 0
	for val in node_list:
		pagerank = val[1]
		if (val[0] in previous_pageranks):
			prev_pr = previous_pageranks[val[0]]
			residuals += (prev_pr - pagerank)**2

	return residuals

input_filename = 'input.txt'
input_filename2 = 'input2.txt'
MAX_ITER = 15
RESIDUAL_THRESHOLD = 0.001 
node_list = []
previous_pageranks = {}
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
		prev_pr = float(info_arr[1])
		previous_pageranks[n_node_id] = prev_pr
		neighbors = list(map(int, info_arr[2:]))
		node_neighbors[n_node_id] = neighbors

# done running, print final results
if iteration == MAX_ITER:	
	res = calculate_residuals(node_list, len(node_list))
	print(res)
	print_final_nodes(node_list)

# not done, write output for next iteration
else:
	res = calculate_residuals(node_list, previous_pageranks)
	if (res <= RESIDUAL_THRESHOLD):
		sys.stdout.write('$'+str(int(iteration)+1)+'\n')
		for node in node_list:
			node_id, pr = node
			prev_pr = 1.0
			if (node_id in previous_pageranks):
				prev_pr = previous_pageranks[node_id]
			write_string = 'NodeId:'+str(node_id)+'\t'+str(pr)+',' + str(prev_pr)
			if node_id in node_neighbors:
				write_string += ','
				out_list = node_neighbors[node_id]
				for i, val in enumerate(out_list):
					write_string += str(val)
					if i + 1 < len(out_list):
						write_string += ','
			sys.stdout.write(write_string+'\n')
		print(res)
		print_final_nodes(node_list)
	else:
		sys.stdout.write('$'+str(int(iteration)+1)+'\n')
		for node in node_list:
			node_id, pr = node
			prev_pr = 1.0
			if (node_id in previous_pageranks):
				prev_pr = previous_pageranks[node_id]
			write_string = 'NodeId:'+str(node_id)+'\t'+str(pr)+',' + str(prev_pr)
			if node_id in node_neighbors:
				write_string += ','
				out_list = node_neighbors[node_id]
				for i, val in enumerate(out_list):
					write_string += str(val)
					if i + 1 < len(out_list):
						write_string += ','
			sys.stdout.write(write_string+'\n')