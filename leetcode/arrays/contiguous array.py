#%%
#nums = [0,1,0,1]
nums=[0,0,1,0,0,0,1,1]

cnt, max_l = 0, 0
hm = {0: -1}
for i in range(len(nums)):
    if nums[i] == 0:
        cnt -= 1
    else:
        cnt += 1

    if cnt in hm.keys():
        max_l = max(max_l, i - hm[cnt])
    else:
        hm[cnt] = i

print(max_l)

#%%



