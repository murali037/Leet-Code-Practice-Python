
nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [1,1,2]

i =0
j = i+1
while i < len(nums):
    print("i: ", i, "j: ", j)
    while j < len(nums):
        print("i: ", i, "j: ",j)
        if nums[i] == nums[j]:
            del nums[i]
            print("after del, nums: ", nums)
            i=0
            j=0
        j = j+1
    print("after j loop ends, nums: ", nums)
    print("i: ", i, "nums[i]:",nums[i])
    i = i+1
    j = i+1

print(nums)