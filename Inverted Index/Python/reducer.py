#!/usr/bin/python

import sys 
import re

word_dict = {}
         
for line in sys.stdin:
        
        # Split the line to extract the word and posting of the record
        word, posting = line.split('\t')
        
        word_dict.setdefault(word, {}) 
              
        # Extract the document id and count from the posting
        doc_id, count = posting.strip().split(':')
        count = int(count)
        
        # Store the document ids for each word and increment the count for each occurence of word in that document
        word_dict[word].setdefault(doc_id, 0)
        word_dict[word][doc_id] += count
  
for word in word_dict:
        postings_list = ["%s:%d" % (doc_id, word_dict[word][doc_id])for doc_id in word_dict[word]]
 
        postings = ','.join(postings_list)
        print('%s\t%s' % (word, postings))
