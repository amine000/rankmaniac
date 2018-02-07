#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
	arr = line.split('\t')
	# compile all nodes and pageranks in this list
	#if int(arr[0]) >= 0:
	sys.stdout.write(str(1)+'\t'+str(arr[0])+','+str(arr[1]))
	# iteration number stored here
	"""
	elif int(arr[0]) == -1:
		sys.stdout.write(str(0)+'\t'+str(arr[0])+','+str(arr[1]))
	# neighbors stored here
	else:
		sys.stdout.write(str(-1)+'\t'+str(arr[0])+','+str(arr[1]))		
	"""