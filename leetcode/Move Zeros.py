#%%
nums = [1,0,1]

i, j = 0, 1
while i < j and j < len(nums):
    if nums[i] == 0 and nums[j] != 0:
        nums[i] = nums[j]
        nums[j] = 0

    elif nums[i] == 0 and nums[j] == 0:
        j += 1
        continue
    i += 1
    j += 1
print(nums)
