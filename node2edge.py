#!/usr/bin/env python

import sys
import optparse
import time
import sys
import os
import subprocess

def main():
    usage = "usage: %prog [options] args"
    op = optparse.OptionParser(usage)

    op.add_option('--input-file', '-i', dest="in_file",\
                     help="input file name, a node list")
    op.add_option('--out-file', '-o', dest="out_file",\
                     help="output file name")

    (options, args) = op.parse_args()
    
    out_file = "edge_list.csv"
    if options.in_file:
        in_file = options.in_file
    else:
        op.print_help()
        sys.exit(1)

    if options.out_file:
        out_file = options.out_file 
    else:
        out_file = "edge_list.csv"

    node = open(in_file, "r")
    edge = open(out_file, "w")


    edge_pair = {}
    node_lines = node.readlines()
  
    attrs = node_lines[0].split(",")
    attrs = [item.strip() for item in  attrs]
    attrs = attrs.remove(attrs[0])    
    length = len(attrs)


    lines = [] 
    first = True 
    for line in node_lines:
        if first:
            first = False
            continue
        words = line.split(",")
        words = [item.strip() for item in words] # strip space and line return
        lines.append(words)

    for line in lines:
        for compare_line in lines:
            if line == compare_line:
                continue
            for i in range(1,length+1):
                if line[i] == compare_line[i]:
                    add(line[0], compare_line[0], attrs[i-1])

def class edges():
    def __init__():
        self.pairs = []     
        self.commons = []
        self.count = []

    def add(a, b, attr):
        for item in self.pairs:
            if a in item and b in item:
                self.commons.append(attr)
            else:
                self.paris.append([a,b])
                self.commons.append(attr)
            

                 
        
        

if __name__ == "__main__":
    main()

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
