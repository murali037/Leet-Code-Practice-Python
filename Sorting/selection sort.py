#%% my method lec 4

A = [11,3,42,28,17,8,2,15]

def sel_sort1(A):
    i=0
    while i < (len(A)-1):
        if A[i] > A[i+1]:
            temp1 = A[i]
            A[i] = A[i+1]
            A[i+1] = temp1
            i=0
        else:
            i += 1
    return A
print("unsorted: ",A)
print("sorted: ",sel_sort1(A))

#%%
