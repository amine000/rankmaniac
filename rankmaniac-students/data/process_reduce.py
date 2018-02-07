#!/usr/bin/env python

import sys
import os

#
# This program simply represents the identity function.
#

input_filename = '/Users/amineboubezari/rankmaniac/rankmaniac-students/data/input.txt'
input_filename2 = '/Users/amineboubezari/rankmaniac/rankmaniac-students/data/input2.txt'
MAX_ITER = 50
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


g = open(input_filename, 'r')
old_lines = []
for line in g:
	old_lines.append(line)
g.close()

if iteration != 0:
	old_lines = old_lines[1:]

f = open(input_filename2, 'w')
f.write('$'+str(int(iteration)+1)+'\n')
for line in old_lines:
	arr = line.split('\t')
	node_id = int(arr[0][7:])
	out_list = [node_dict[node_id], 0.0] + arr[1].split(',')[2:]
	f.write(str(arr[0])+'\t')
	for i, val in enumerate(out_list):
		f.write(str(val))
		if i + 1 < len(out_list):
			f.write(',')

f.close()

os.remove(input_filename)
os.rename(input_filename2, input_filename)