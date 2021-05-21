#!/usr/bin/python3
import sys
import logging

logging.getLogger().setLevel(logging.INFO)

cur_node = None
prev_node = None
adj_list = []

logging.info(sys.argv[1])
pr = open(sys.argv[1], 'w')


for line in sys.stdin:
    cur_node, dest_node = line.strip().split(',')
    if cur_node == prev_node:
        adj_list.append(dest_node)
    else:
        if prev_node:
            print(prev_node, ",".join(sorted(adj_list)), sep="\t")
            pr.write(str(prev_node) + ",1\n")
        prev_node = cur_node
        adj_list.clear()
        adj_list.append(dest_node)

if cur_node == prev_node:
    print(prev_node, ",".join(sorted(adj_list)), sep="\t")
    pr.write(str(prev_node) + ",1\n")

pr.close()
