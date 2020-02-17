
# 1. Two Sums - Brute Force

# time limit exceeded for this
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] != target or i == j:
#                     continue
#                 else:
#                     return [i, j]



#%%
# 1. Brute Force - accepted sol - O(n^2)
nums = [2,7,11,15]
target = 9


def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twoSum(nums, target))

len(nums)

for i in range(len(nums)-1):
 print("i=",i)
  for j in range(i + 1, len(nums)):
    print("j=",j)

# how the loop works
# i= 0
# j= 1
# j= 2
# j= 3
#
# i= 1
# j= 2
# j= 3
#
# i= 2
# j= 3
#%% using hashmap
target = 9
nums = [5, 67, 3, 7, 34, 8, 9, 2, 11, 15]
h = {}
print(h)
for i, num in enumerate(nums):
    n = target - num
    print('i= ', i, "target-num= ", n)
    if n not in h:
        h[num] = i
        print("dict= ", h)
    else:
        print([h[n], i])
        break



#%% Dictionaries

d = {}
l = []

d[1] = "yes"
d["1"] = "No"

#%%
d

class my_class:
    def __init__(self):
        self.data = "data"


instance = my_class()

d['object'] = instance

d.keys()
d.items()
#%%

for key in d.keys():
    print(key)

for key, value in d.items():
    print("key:", key, "value:", value)
