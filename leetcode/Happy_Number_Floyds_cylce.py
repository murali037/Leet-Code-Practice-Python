#%% Hash set
def happy(n):
    tot_sum = 0
    while n > 0:
        n, ones = divmod(n, 10)
        tot_sum += ones ** 2
        #print("n:", n, "ones:", ones, "divmod:", divmod(n, 10), "sum:", tot_sum)
    return tot_sum

n=19
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = happy(n)
    print("n:", n)
if n == 1:
    print('true')
else:
    print('false')

#%% Floyd's cycle finding algorithm

def get_next(n):
    tot_sum = 0
    while n > 0:
        n, ones = divmod(n, 10)
        tot_sum += ones ** 2
    # print("n:",n,"ones:",ones,"divmod:",divmod(n,10),"sum:", tot_sum)
    return tot_sum

n=19
slow_runner = n
fast_runner = get_next(n)
print("initial", "f:", fast_runner, "s:", slow_runner)
while fast_runner != 1 and slow_runner != fast_runner:
    slow_runner = get_next(slow_runner)
    fast_runner = get_next(get_next(fast_runner))
    print("while", "f:", fast_runner, "s:", slow_runner)

if fast_runner == 1:
    print('true')
else:
    print('false')


