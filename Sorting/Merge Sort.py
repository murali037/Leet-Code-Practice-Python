#%%


def MS(A):
    """Sorts a list using recursion and helper merge function."""
    if len(A) < 2:
        return A

    mid = len(A) // 2

    L = MS(A[0:mid])
    R = MS(A[mid:len(A)])

    print("MS - ","L: ",L,"R: ", R)

    return merge(L,R)


def merge(L, R):
    """Merges two sorted lists"""

    i = 0
    j = 0
    res = []
    #print("Merge - ", "L: ",L, "R: ", R)
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res.append(L[i])
            i += 1
            print("Merge L[i] < R[j] - ", "L: ",L,"i: ",i,"R: ", R,"j: ",j,"Res: ", res)
        else:
            res.append(R[j])
            j += 1
            print("Merge L[i] > R[j] - ", "L: ", L,"i: ",i, "R: ", R,"j: ",j, "Res: ", res)

    while i < len(L):
        res.append(L[i])
        i += 1
        print("Merge i < L - ", "i: ", i, "L: ", L, "Res: ", res)

    while j < len(R):
        res.append(R[j])
        j += 1
        print("Merge j < R - ", "j: ", j, "R: ", R, "Res: ", res)

    return res

A = [5,4,2,1]

print("unsorted list: ", A)
print("Sorted list: ", MS(A))