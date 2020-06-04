#%%

def LCP(A):
    if len(A) == 0:
        return ""

    if len(A) == 1:
        return A[0]

    # divide and conquer strategy

    mid = len(A) // 2

    # Divide step
    L = LCP(A[:mid])  # A will have index from 0 to mid-1 here
    R = LCP(A[mid:])

    # Conquer step
    print("LCP - ", "L: ", L, "R: ", R)
    return merge(L, R)


def merge(L, R):
    s = 0
    while s < len(L) and s < len(R) and L[s] == R[s]:
        print("merge:")
        print("s: ", s, "len(L): ", len(L), "len(R): ", len(R), "L[s]: ", L[s], "R[s]: ", R[s])
        s += 1
        print("After increment of s: ", "L[:s]: ", L[:s])
    return L[:s]


A = ['bottle', 'bottle', 'bottle']
#A = ['bottle', 'bottle', 'bottle', 'bottle', 'bottle', 'bottle']

print(A)
res = LCP(A)
print(res)

#%%

rows = [[] for i in range(2 ** 2)]

for i in range(2**2):
      rows[i] = [0] * 2**2

rows[1][2] = -1
