def aif(x,l):
    """ 
    This is a help function. It takes a character and list
    as arguments. It then inserts the character in front of all
    other characters in the given list, and return the list.
    """
    for i in range(len(l)):
            l[i].insert(0, x)
    return l

def bitstr(n):
    if n == 0: return [] # Base case of n = 0
    if n == 1: return [[0],[1]] # Base case of n = 1
    if n == 2: return [[0,0],[0,1],[1,0],[1,1]] # Base case of n = 2
    else:
        # Using recursion to find the next bitstrings by taking the
        # previous bitstring twice. First time we add "0" in front of
        # all the elements in each list, and the second time we add "1"
        # to all elements in each list. We do this by calling our help
        # function "aif".
        return (aif(0, bitstr(n-1)) + aif(1, bitstr(n-1)))

def printbitstring(n):
    # Iterate though n and the bitstr function to print the result.
    for elt in bitstr(n):
        print elt

print printbitstring(0)
print printbitstring(1)
print printbitstring(2)
print printbitstring(3)
print printbitstring(4)
print printbitstring(5)                    
