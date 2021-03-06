# O(2^n)
def genSubsets(L):
    res = []
    if len(L)==0:
        return ( [] )
    smaller = genSubsets(L[:-1])
    extra   = L[-1:]
    new     = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new

L=[1,2,3,4,5,6,7,8,9]
print(genSubsets(L))
