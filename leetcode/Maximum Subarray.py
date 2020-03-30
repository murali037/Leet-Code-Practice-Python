#%%

#Brute force approach

nums = [2,-1,3,-7,-2]
nums = [-2,-1]
sums = {}
c=0
for i in range(len(nums)):
    d=0
    print("i: ", i)
    for j in range(i,len(nums)):
        print("j: ", j, "c: ", c, "d: ", d, "nums[j]: ", nums[j])
        sums[c] = d + nums[j]
        print("sums: ", sums[c], "c: ",c)
        c += 1
        d = sums[c-1]
print(max(sums.values()))

