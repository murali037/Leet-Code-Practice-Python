#%%
n = 102

def rec(n,c,h):
    print('recursion happening')
    c=c
    h=h
    print("c:",c)
    # if c == 20:
    #     return 0
    m = list(str(n))
    x=0
    for i in range(len(m)):
        m[i] = int(m[i])
        x += m[i]**2
    print("x: ", x)
    print("h: ", h)
    if x == 1:
        return(print('TRUE'))
    if x in h.values():
        return(print('FALSE'))
    h[c] = x
    c +=1
    rec(x,c,h)


c=0
h={}
rec(n,c,h)

#%%


def Sol(n):

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
            print("n: ",  n, "digit: ", digit, " sum: ", total_sum)
        return total_sum


    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1

n = 102
print(Sol(n))

