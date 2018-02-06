#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
	arr = line.split('\t')
	sys.stdout.write(str(1)+'\t'+str(arr[0])+','+str(arr[1]))

