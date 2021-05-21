#!/usr/bin/python

import sys

# Read the input from the STDIN one line at a time
for line in sys.stdin:
    
    # Split the input line to constituent words 
    words = line.split()
    
    # For each word in the line generate a new key-value record like
    # where the key is the word and value is 1
    # Each new key-value records will be written in a line 
    # and will be separated by tab
    for word in words:
        print('{}\t{}'.format(word, 1))