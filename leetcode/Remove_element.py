nums = [0,1,2,2,3,0,4,2]
val = 2
sub = 0
c = 0
for i in range(len(nums)):
    print("i: ", i, "c: ", c)
    if (i == len(nums) - 1):
        if (nums[i] == val):
            sub += 1
    elif ((nums[c] == val) and (i != len(nums) - 1)):
        nums[c] = nums[i + 1]
        sub += 1
        print("if nums: ",nums)
    elif((nums[c] == val) and (i == len(nums)-1)):
        sub += 1
        break;
    else:
        c += 1
        nums[c] = nums[i+1]
        print("else nums: ", nums)
print(len(nums) - sub)
print(nums[0:len(nums) - sub])
