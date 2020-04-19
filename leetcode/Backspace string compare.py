#%%

S = "ab#c"
T = "ad#c"

s1, t1 = list(S), list(T)
s2, t2 = [], []

for i in range(len(s1)):
    if s1[i] == "#":
        if len(s2) == 0:
            continue
        else:
            s2.pop()
    else:
        s2.append(s1[i])

for i in range(len(t1)):
    if t1[i] == "#":
        if len(t2) == 0:
            continue
        else:
            t2.pop()
    else:
        t2.append(t1[i])

if len(s2) != len(t2):
    return 0

if s2 == [] and t2 == []:
    return 1

for i in range(len(s2)):
    if s2[i] != t2[i]:
        return 0
return 1




#%% str pop?

S = "ab#c"
s1=list(S)
print(s1)
s1.pop()
print(s1)

