
def doubleLast(j):
    w= len(j)
    j[len(j)-1]= w
    j.append(w)
    return j
print (doubleLast([1, 2, 3, 4, 5]))