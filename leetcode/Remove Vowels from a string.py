#%%

S = "leetcodeisacommunityforcoders"

vow = ['a', 'e', 'i', 'o', 'u']
c = ""
for elem in S:
    if str(elem) in vow:
        continue
    c += elem
print(c)
