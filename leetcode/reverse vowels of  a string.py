#%%

S = "Noel sees Leon."

s = list(S)
l,r = 0,len(s)-1
vow = ['a','e','i','o','u','A','E','I','O','U']

# if s == "":
#     return ""
# elif len(s) == 1:
#     return s

while l != r:
    if s[l] in vow:
        if s[r] in vow:
            s[l],s[r] = s[r],s[l]
            if r - l == 1:
                break
            l +=1
            r -=1
            continue
        r -=1
        continue
    l +=1
res = "".join(s)
print(res)