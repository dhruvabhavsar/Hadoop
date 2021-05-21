#!/usr/bin/python3
import sys
import logging

logging.getLogger().setLevel(logging.INFO)

count=0

for line in sys.stdin:
    count+=1
    if line.startswith('#'):
        continue
    else:
        print(",".join(line.strip().split()))
