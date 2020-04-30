#%%
s=['h','e','l','l','o']
l, r = 0, len(s) - 1
while l != r:
    if len(s) == 0:
        break
    elif len(s) == 1:
        break
    s[l], s[r] = s[r], s[l]
    if r - l == 1:
        break
    l += 1
    if r - l == 1:
        break
    r -= 1
print(s)
