
# Insertion Sort - step by step disection

step 1

def insertion_Sort(a):
    temp = []
    for i in range(len(a)-1):
        print("i= ", i)
        if(a[i] > a[i+1]):
            print("before, a[i]= ",a[i]," a[i+1]= ",a[i+1])
            temp = a[i+1]
            a[i+1] = a[i]
            a[i] = temp
            print("after, a[i]= ", a[i], " a[i+1]= ", a[i + 1])
    return a




# Input Array
x = [1, 3, 5, 6, 3, 6, 32, 2, 8]

res = insertion_Sort(x)
print("res:", res)

############################################################################################################################################################################################

#step 2 - at first stop, add another operation

def insertion_Sort(a):
    temp = []
    i=0
    while i <(len(a)-1):
        print("i= ", i)
        if (a[i] > a[i + 1]):
            print("before, a[i]= ", a[i], " a[i+1]= ", a[i + 1])
            temp = a[i + 1]
            a[i + 1] = a[i]
            a[i] = temp
            print("after, a[i]= ", a[i], " a[i+1]= ", a[i + 1])
            print(a)
            i-=2
        i+=1
    return a


# Input Array
x = [1, 3, 5, 6, 3, 6, 32, 2, 8]

res = insertion_Sort(x)
print("res: ", res)