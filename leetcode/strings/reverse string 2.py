#%%
L = [0,1,2,3,4,5,6,7,8,9]
print(L[::-1][::2])

#%%
s = "abcdef"
i=0
k=3
t1 = ""
length = len(s)
while i<=len(s):
    t1 += s[i:i+2*k][0:k][::-1] + s[i+k:i+2*k]
    i += 2*k
    print(i, "   ", t1)

print(t1)
