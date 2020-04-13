#%%

str = ["eat", "tea", "tan", "ate", "nat", "bat"]

Anagrams = {}
for k in str:
    key = "".join(sorted(k))
    if key not in Anagrams:
        Anagrams[key] = [k]
    else:
        Anagrams[key].append(k)
print(Anagrams.values())