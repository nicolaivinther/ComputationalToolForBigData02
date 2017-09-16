def aif(x,l):
    for i in range(len(l)):
            l[i].insert(0, x)
    return l
"""
lst = [[0,0],[0,1],[1,0],[1,1]]
lste = [[0,0],[0,1],[1,0],[1,1]]
print aif(0,lst)
print aif(1,lste)

"""
def bitstr(n):
    if n == 0: return []
    if n == 1: return [[0],[1]]
    if n == 2: return [[0,0],[0,1],[1,0],[1,1]]
    else:
        return (aif(0, bitstr(n-1)) + aif(1, bitstr(n-1)))

"""                    
print bitstr(0)
print bitstr(1)
print bitstr(2)
print bitstr(3)
print bitstr(4)
print bitstr(5)
"""

def printbitstring(n):
    for elt in bitstr(n):
        print elt


print printbitstring(0)
print printbitstring(1)
print printbitstring(2)
print printbitstring(3)
print printbitstring(4)
print printbitstring(5)                    
