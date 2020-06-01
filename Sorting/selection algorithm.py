#%%
import math

A = [11,3,42,28,17,8,2,14,15,87]
piv = A[0]

def Median(A,piv):

    res = [0]*len(A)
    l,r = 0,len(A)-1
    for i in range(len(A)):
        if A[i] < piv:
            res[l] = A[i]
            l +=1
        elif A[i] > piv:
            res[r] = A[i]
            r -= 1
    idx = l
    res[idx] = piv
    print(res, "   ", idx)
    if idx == math.ceil(len(A)/2):
        return 1
    elif idx > math.ceil(len(A)/2):
        Median(res,res[idx-1])
    else:
        Median(res,res[idx+1])

med = Median(A,piv)
print(med)