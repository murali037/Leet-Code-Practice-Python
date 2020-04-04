#%%
A = [1,24,22,3,5,2,677,34,5,99,32,4,5,4,67,4,234,3]

def Binary_Search(nums,p):
    l = len(nums)
    x=0
    for i in range(l):
        if x != p:
            x = nums[round(l/2)]

    return i

a = Binary_Search(A,234)
print(A[a])




#%%

A = [1,24,22,3,5,2,677,34,5,99,32,4,5,4,67,4,234,3]


def Bin_search(n,p):
    nums=n
    l = len(nums)
    print("l:",l)
    mid = round(l/2)
    if p == nums[mid] or l ==1:
        print("mid:",mid)
        return mid
    elif p < nums[mid]:
        print("left",nums[mid])
        Bin_search(nums[0:mid+1],p)
    elif p > nums[mid]:
        print("right",nums[mid])
        Bin_search(nums[mid:len(nums)+1],p)


print(Bin_search(A,234))
