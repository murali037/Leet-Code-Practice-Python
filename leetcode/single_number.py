#%%
nums = [2,2,1]

d ={}
for i in range(len(nums)):
    print("i: ",i, "nums: ",nums[i],"d:",d)
    if nums[i] in d.keys():
        d.pop(nums[i])
        print(d)
    else:
        d[nums[i]] = i
for x,y in d.items():
print(x)