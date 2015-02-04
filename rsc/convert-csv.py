#!/usr/bin/env python3

import csv
from sys import argv
from os import path

if (len(argv) != 2):
	print("expecting one argument: filename")
	exit(1)

filename = argv[1];

if (not path.isfile(filename)):
	print(filename + " is not a file")
	exit(2)


def escape(text):
	r = text[:]
	for i in range(0, len(text)):
		r[i] = text[i].replace("_", "\\_")
	return r


with open(filename, 'r') as f:
	reader = csv.reader(f, delimiter=',', quotechar='"')
	i = 0
	for row in reader:
		row = escape(row)
		i = i + 1
		if (i <= 2): continue
	
		print(row[0] + " & ", end='')
		print(row[1], end="")
		if row[2]: print(" " + row[2], end="")
		print(", " + row[3], end="")
		print(" & " + row[4] + " \\\\ \\hline")

