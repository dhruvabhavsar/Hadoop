#!/usr/bin/python3
import sys

cur_node = None
prev_node = None
contrib_sum = 0

k=0.15/875713

for line in sys.stdin:
    cur_node, contrib = line.strip().split(',')

    if cur_node == prev_node:
        contrib_sum += float(contrib)
    else:
        if prev_node:
            new_pr = k+0.85 * contrib_sum
            print(prev_node, new_pr, sep=', ')
        prev_node = cur_node
        contrib_sum = float(contrib)

if cur_node == prev_node:
    new_pr = k+0.85 * contrib_sum
    print(prev_node, new_pr, sep=', ')
