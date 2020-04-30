#%%

arr = [8,7,12,13,0,6,8,10,0,0,0,6,0,14]
arr = sorted(arr)
l,r = 0,1
c=0
while r < len(arr):
    if arr[r]==arr[l]+1:
        c+=1
        l+=1
        r=l+1
    elif arr[l]==arr[r]:
        r+=1
    else:
        l+=1
        r=l+1
print(c)
