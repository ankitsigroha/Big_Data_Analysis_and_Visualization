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


    topten = ["gun","york", "school","people", "students", "nra", "advertisement","violence", "shooting", "think", "high"]

    words = line.split()
    # increase counters

    for i in range(len(words) - 1):
        if words[i] in topten:
            for j in range(i,len(words) - 1): 
                if words[j] in topten and words[i] != words[j]:

                    if(words[i] > words[j]):
                        print '%s\t%s' % (words[i]+":"+words[j], 1)
                    else:
                        print '%s\t%s' % (words[j]+":"+words[i], 1)

