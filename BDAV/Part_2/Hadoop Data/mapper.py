#!/usr/bin/env python
import sys
import nltk
import re
from stop_words import get_stop_words

stop_words = get_stop_words('en')
stop_words = get_stop_words('english')




# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words

    line = line.lower()
    line = line.replace(",","")
    line = line.replace("?","")
    line = line.replace("!","")
    line = line.replace("#","")
    line = line.replace('"','')
    line = line.replace(";","")
    line = line.replace("%","")
    line = line.replace('|',' ')
    line = line.replace("-","")


    additional = ["will", "won't", "wont", "ain't", "aint", "don't", "dont", "didn't", "didnt", "many", "we", "us", "tweet"]

    words = line.split()
    # increase counters

    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        

        

        if re.search(r"^[\.\,\?\<\>\!\@\'\"]", word):
        	word = word[1:]

        word = re.sub(r"([\.\'\"\?\!\,\:\=\(\)\\\/\-\+\$\*\[\]\_]*)([\w\W]+)",r"\2",word)
        word = re.sub(r"([\.\'\"\?\!\,\:\=\(\)\\\/\-\+\$\*\[\]\_]*)$",r"", word)

        if word == "rt":
        	continue
        if re.search(r"\<(.)*\>", word):
        	continue
        if re.search(r"^[\@\&](.)*", word):
        	continue
        if re.search(r"[\d]+", word):
        	continue
        if re.search(r"^http", word):
        	continue
        if word.isspace() or word == "":
        	continue
        
        if word not in stop_words and word not in additional :
        	word = word.replace("'","")
        	word = word.replace('"','')
        	print '%s\t%s' % (word, 1)