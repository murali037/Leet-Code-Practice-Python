#%% using integer division

#nums = [1,2,3,4]
#Output: [24,12,8,6]
nums = [1, 1]

h = {}
prev,idx = 1,0
res = []
for i in range(len(nums)):
    if nums[0] ==0:
        h[i]=0
    elif nums[i]==0:
        h[i] = prev
    else:
        h[i] = nums[i] * prev
        prev = h[i]
        idx =i
print(h)
if max(h.values()) ==0:
    res = nums
else:
    for i in range(len(nums)):
        if nums[i] ==0:
            res.append(h[idx])
        elif nums[i] == 1:
            if max(h.values())==1:
                res.append(0)
            else:
                res.append(max(h.values()))
            print(i, res)
        else:
            res.append(int(h[idx] / nums[i]))


print(res)

#%%

nums = [1,2,3,4]
#Output: [24,12,8,6]

h = {}
prev = 1
res = []
for i in range(len(nums)):
    h[i] = nums[i] * prev
    prev = h[i]

for i in range(len(nums)):
    res.append(int(h[3]/nums[i]))

print(res)
