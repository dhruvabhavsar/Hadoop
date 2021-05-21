#!/usr/bin/python3
import sys

pageranks = {}  

with open(sys.argv[1], 'r') as pr:
    for line in pr:
        node, rank = line.strip().split(',')
        pageranks[node] = rank

for line in sys.stdin:
    node, adj_list = line.strip().split('\t')
    adj_list = adj_list.split(',')
    out_num = len(adj_list)     

    print(node, '0.0', sep=',')    
    for out_link in adj_list:
        out_link_contrib = float(pageranks[node]) / out_num
        print(out_link, str(out_link_contrib), sep=',')
