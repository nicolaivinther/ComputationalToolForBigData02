def char_hist( dictionary, string ):
    """
    This function checks how many times each letter exists in a string.
    """
    for letter in string:
        # If the letter is already a key in the dictionary, we add
        # one to the keys value. If it doesn't exist, we create the
        # letter as a new key, and set the value to 0.
        key = dictionary.get(letter, 0)
        dictionary[letter] = key + 1 # Adds one to the key value
    print dictionary

# Two examples to see if the function works as expected.
print  # blank line
print 'Testing char_hist( histogram, "testing stuff")'
histogram = {}
print 'Where histogram = {}'
print "Expected: {' ': 1,  e: 1,  g: 1,  f: 2,  i: 1,  n: 1,  s: 2,  u: 1,  t: 3}"
print 'Actual:', char_hist( histogram, "testing stuff" ) 

print  # blank line
print 'Testing char_hist( histogram, "more testing")'
histogram = {' ': 1, 'e': 1, 'g': 1, 'f': 2, 'i': 1, 'n': 1, 's': 2, 'u': 1, 't': 3}
print "Where histogram = {' ': 1, 'e': 1, 'g': 1, 'f': 2, 'i': 1, 'n': 1, 's': 2, 'u': 1, 't': 3}"
print "Expected: {' ': 2,  e: 3,  g: 2,  f: 2,  i: 2,  m: 1,  o: 1,  n: 2,  s: 3,  r: 1,  u: 1,  t: 5}"
print 'Actual:', char_hist( histogram, "more testing" )
