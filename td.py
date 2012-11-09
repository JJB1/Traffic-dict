from sys import argv
import sys
import re

dictionary = {}
with open("traffic-dict.txt") as f:
    for line in f:
       (key, val) = line.split()
       dictionary[str(key)] = val 
 
def replace_words(text, word_dic):
    rc = re.compile('|'.join(map(re.escape, word_dic)))
    def translate(match):
        return word_dic[match.group(0)]
    return rc.sub(translate, text)
	   
file = open(sys.argv[1], 'r+', 0)
input = file.read()
file.close()
 
output = open('output', 'w') 
 
results = replace_words(input, dictionary)
 
output.write(results) 