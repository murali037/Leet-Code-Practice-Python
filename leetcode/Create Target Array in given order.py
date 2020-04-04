#%%
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
import numpy as np
res = list(np.zeros(len(nums), dtype = 'int8'))
h={}
for i in range(len(nums)):
    if index[i] in h.keys():
        temp1 = res[index[i]]
        res[index[i]] = nums[i]
        c = index[i]
        print("c:", c)
        if c != len(nums)-1:
            print("c:", c, "len:", len(nums))
            for j in range(c,len(nums)):
                print("j",j)
                if j + 2 < len(nums):
                    temp2 = res[j+2]
                    res[j+1] = temp1
                    print("j",j, res, "temp2:", temp2)
                    temp1 = temp2
                else:
                    if j+1 < len(nums):
                    res[j+1] = temp1

    res[index[i]] = nums[i]
    h[index[i]] = nums[i]
    print(res, h)
print(res)

