import os
import json
from pprint import pprint

os.chdir("/Users/Nicolai/Dropbox/KU/10. Semester/Computational tool for big dataset")
with open('pizza-train.json') as data_file:
    data = json.load(data_file)

def get_text(key):
    newlist = []
    for elt in range(len(data)):
        newlist.append(data[elt][key])
 #   newlist = map( str.lower, newlist )
    print newlist[0:2]
    return newlist

get_text('request_text')
