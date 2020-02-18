#%% Search Insert position

class solution:

    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                continue
            else:
                return i
        return i + 1


nums = [1,3,5,6]
target = 0

print(solution().searchInsert(nums,target))

#%%
class solution:

    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

nums = [1,3,5,6]
target = 0

print(solution().searchInsert(nums,target))

#%%

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = [1, 2, 5, 5, 6, 6, 7, 7, 8, 9]
        k = 7
        x = 7
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            print("mid= ", mid, "arr[mid]= ", arr[mid], "X= ", x)
            if arr[mid] == x:
                index = mid
                print("idx= ", index)
                break
            elif l == r:
                index = l
                break
            elif arr[mid] > x:
                if mid == l:
                    r = l
                    index = r
                else:
                    r = mid - 1
                    print("r= ", r)
                    index = r
            else:
                if mid == r:
                    l = r
                    index = l
                else:
                    l = mid + 1
                    print("l= ", l)
                    index = l
        print("index= ", index)
        try:
            lower = abs(x - arr[index - 1])
            print("lower= ", lower)
            higher = abs(x - arr[index + 1])
            print("higher= ", higher)
            middle = abs(x - arr[index])
            print("middle= ", middle)

            if min(lower, middle, higher) == higher:
                index = index + 1
            elif min(lower, middle, higher) == middle:
                index = index
            else:
                index = index - 1
        except:
            index = index
        print("final_index=", index)

        op = []
        count = 0
        if (index - k + 1) < 0:
            start_index = 0
        else:
            start_index = (index - k + 1)
        for i in range(start_index, (index + k)):
            count += 1
            if count == k + 1:
                break
            try:
                op.append(arr[i])
                print("i= ", i, "count= ", count, "op= ", op)
            except:
                count -= 1
                print("i= ", i, "count= ", count, "op= ", op)

        return op

#%%
