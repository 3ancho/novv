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
    node.close()
  
    attrs = node_lines[0].split(",")
    print attrs
    attrs = [item.strip() for item in  attrs]
    print attrs
    attrs.remove(attrs[0])    
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

    edge_list = Edges() 
    for line in lines:
        i = lines.index(line)
        for compare_line in lines[i:]:
            if line == compare_line:
                continue
            for i in range(1,length+1):
                if line[i] == compare_line[i]:
                    edge_list.add(line[0], compare_line[0])

    edge.write("Source,Target,Count\n")
    for item in edge_list.pairs:
        edge.write("{},{},{}\n".format(item['name'][0],\
                                       item['name'][1],\
                                       item['count']))
    edge.close()

class Edges():
    def __init__(self):
        self.pairs = []     

    def add(self, a, b, attr=""):
        e = {}
            
        for i in range(0,len(self.pairs)):
            if a in self.pairs[i]['name'] and b in self.pairs[i]['name']:
                self.pairs[i]['count'] += 1
                return
        e['name'] = (a,b)
        e['count'] = 1
        self.pairs.append(e)
        

if __name__ == "__main__":
    main()

