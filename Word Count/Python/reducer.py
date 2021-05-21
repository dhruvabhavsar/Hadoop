#!/usr/bin/python

import sys

# Initialize the auxiliary variables 
last_key = None # Auxiliary variable to detect the first word in the input   
last_key_count = 0 # Auxiliary variable to keep the count of a word so far 

# Read sorted intermediate key-value records one line at a time from the STDIN
# Each line is a tab separated key-value record generated in the map phase
for line in sys.stdin:
    
    # Split the line to extract the key and value parts of the record
    key,value = line.split('\t',1)
    
    # Compare the ket with the last key we have read so far to see if 
    # we are reading a new word
    if last_key != key:
        
        # If we are reading a new word and the previous word is not None
        # write the previous word and its count in a line separated by tab 
        if last_key:
            print('{}\t{}'.format(last_key,last_key_count)) 
        
        # Reset the auxiliary variables 
        last_key = key
        last_key_count = 0 
        
    # Add the count of the word to the auxiliary variable     
    last_key_count += int(value)


# Print the count of the last word in if it is not None
if last_key:
    print('{}\t{}'.format(last_key,last_key_count))