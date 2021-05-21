#!/usr/bin/python

import sys 
import re
import os

for line in sys.stdin:

        # Get the path of the file and get the file name
        doc_id = os.environ["map_input_file"]
        doc_id = re.findall(r'\w+', doc_id)[-1]

        # Get a list of words in the documents
        words = line.split()

        # Map the words with document id 
        for word in words:
                print("%s\t%s:1" % (word, doc_id))