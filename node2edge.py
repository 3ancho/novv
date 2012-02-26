#!/usr/bin/env python

import sys

node = open("hello.csv", "r")
edge = open("out_edge.csv", "w")

major = []
year = []

node_lines = node.readlines()

lines_lists = []

first = True 
for line in node_lines:
    if first:
        first = False
        continue
    words = line.split(",")
    words = [item.strip() for item in words] # strip space and line return
    lines_lists.append(words)
    if words[2] not in year:
        year.append(words[2])
    if words[3] not in major:
        major.append(words[2])

for line in lines_lists:
    major = line[3]
    year = line[2]
    for compare_line in lines_lists:
        if major == compare_line[3]:
            write_line = "{0},{1},{2}\n".format(line[0],compare_line[0],major)
            edge.write(write_line)
        if year == compare_line[2]:
            write_line = "{0},{1},{2}\n".format(line[0],compare_line[0],year)
            edge.write(write_line)

node.close()
edge.close()

sys.exit(0)
