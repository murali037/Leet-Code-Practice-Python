#%% my method lec 4 - insertion sort
import time

t0 = time.time()

A = [11,3,42,28,17,8,2,15,3,4,5,3,5,3,5,3,5,35,5,3,5,35,5,3,5,35,35,355,3,53,53,34,5,3]

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

t1 = time.time()
print("unsorted: ",A)
print("sorted: ",sel_sort1(A))
print("time required:", t1-t0)

#%% a better insertion sort

t0 = time.time()

A = [11,3,42,28,17,8,2,15,3,4,5,3,5,3,5,3,5,35,5,3,5,35,5,3,5,35,35,355,3,53,53,34,5,3]

def sel_sort1(A):
    i=0
    while i < (len(A)-1):
        if A[i] > A[i+1]:
            temp1 = A[i]
            A[i] = A[i+1]
            A[i+1] = temp1
            i = max(i-1,0)
        else:
            i += 1
    return A
t1 = time.time()

print("unsorted: ",A)
print("sorted: ",sel_sort1(A))
print("time required:", t1-t0)


#%% Selection sort - intermediate step

t0 = time.time()

A = [11,3,42,28,17,8,2,15]
res=[]
d=0
g_min = {}
g_min[0] = 9999999
def sel_sort1(A,d,g_min,res):

    for i in range(d,len(A)-1):
        if A[i] < min(A[i+1], g_min[max(g_min.keys())]):
            g_min[i] = A[i]
        elif A[i+1] < g_min[max(g_min.keys())]:
            g_min[i+1] = A[i+1]

   # print("g_min: ", g_min, "max_key: ",max(g_min.keys()), "d: ", d, "A: ", A)

    while d < len(A)-1:
        temp1 = A[d]
        A[d] = g_min[max(g_min.keys())]
        print("d: ", d, "A[d]: ", A[d], "g_min: ", g_min)
        #print(A[max(g_min.keys())])
        A[max(g_min.keys())] = temp1
        d += 1
        g_min = {}
        g_min[0] = 9999999
        print("A: ", A, "d: ", d, "g_min: ", g_min)
        if d == len(A)-1:
            print("Sorted")
            break
        sel_sort1(A,d,g_min,res)
    return A

t1 = time.time()

print("unsorted: ",A)
print("sorted: ",sel_sort1(A,d,g_min,res))
print("time required:", t1-t0)

#%%

d = {0:1,1:2}

max(d.keys())


#%% Selection sort - final working

A = [11,3,42,28,17,8,2,15]

g_min = {}
g_min[0] = 9999999

def sel_sort1(A,g_min):

    def traversal(A, cnt, g_min):
        for i in range(cnt,len(A)-1):
            if A[i] < min(A[i+1], g_min[max(g_min.keys())]):
                g_min[i] = A[i]
            elif A[i+1] < g_min[max(g_min.keys())]:
                g_min[i+1] = A[i+1]
        return g_min

    # set index as cnt
    cnt = 0

    # initial traversal
    if cnt == 0:
       g_min = traversal(A, cnt, g_min)

    while True:
        temp1 = A[cnt]
        A[cnt] = g_min[max(g_min.keys())]
        A[max(g_min.keys())] = temp1

        #increment index and set global min to 0
        cnt += 1
        g_min = {}
        g_min[0] = 9999999

        # traverse again from next index
        g_min = traversal(A, cnt, g_min)

        # do while break
        if cnt == len(A)-1:
            break
    return A

print("unsorted: ",A)
print("sorted: ",sel_sort1(A,g_min))

