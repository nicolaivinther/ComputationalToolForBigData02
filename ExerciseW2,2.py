# -*- coding: utf-8 -*-
import os
import json
import re

os.chdir("/Users/Nicolai/Dropbox/KU/10. Semester/Computational tool for big dataset")
with open('pizza-train.json') as data_file:
    data = json.load(data_file)



def get_uniqe_words(key):
    # This function will return a list cosisting of all
    # uniqe words from every single review in the json file.
    newstring= unicode() # Empty string
    for elt in range(len(data)): # Iterate through all dicts
         newstring += data[elt][key] # Append string to newstring
    newstrlow = newstring.lower() # Turn to lowercase letters
    newstrlow = newstrlow.replace("\n", "") # Remove new lines
    # Remove non-aplhabetic characters but space
    newstralpha = re.sub("[^a-zA-Z ]+", "", newstrlow)
    newlist = newstralpha.split()
    # Converting the list into a set() to only get the uniqe words
    uniqeset = set(newlist)
    # Converting set back to list
    uniqelist = list(uniqeset)
    return uniqelist
#get_uniqe_words('request_text')

def create_list(key):
	# This function will return a list of lists, where each list
	# cosists of all words in every singe review.
    l = [] # Creating empty list to contain all reviews
    for i in range(len(data)):
	    l.append(data[i][key])
	    l[i] = l[i].lower() # Make lowercase letters
	    l[i] = l[i].replace("\n", "") # Remove new lines
	    # Remove non-alphabetic characters bu space
	    l[i] = re.sub("[^a-zA-Z ]+", "", l[i])
	    # Turn string into list
	    l[i] = l[i].split()
    return l
#create_list('request_text')

# Call the uniqe word function, to get the list of uniqe words
countlist = get_uniqe_words('request_text')
# Call the create list function, to get the list of all reviews
reviewlist = create_list('request_text')
# Create an array with (Number of revies x Number of uniqe words)
lists = [[] for _ in range(len(create_list('request_text')))]

# Iterate through Number of reviews
for review in range(len(reviewlist)):
	# Iterate through Number of words
    for elt in range(len(countlist)):
    	# Count each uniqe words occurrences in each review
	    count = reviewlist[review].count(countlist[elt])
	    # Append the count to each reviews list
	    lists[review].append(count)

# Printing the result
print len(lists) # Print number of reviews
print len(lists[5]) # Print number of uniqe words
# Print all word counts from words in review six that appears at least once
for index, value in enumerate(lists[5]):	
	if value > 0:
		print(index, value)