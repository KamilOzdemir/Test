
def capitalise(x):
    a = list(x)
    b=[]
    for t in range(len(a)):
        if t%2 == 0:
            b.append(a[t].upper())
        else:
            b.append(a[t].lower())  
        if t == len(a):
            break
    return (''.join(b))
