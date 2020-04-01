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

##########################################################################################################################################################
# Optimise - Kadane's algorithm

nums = [2,-1,3,-7,-2]
local_max = nums[0]
global_max = nums[0]

for i in range(1,len(nums)):
    print("i: ", i, "local_max: ", local_max)
    local_max = max(nums[i], nums[i]+local_max)
    if local_max > global_max:
        global_max = local_max

print(global_max)






