
## first try - missed an edge case

height = [1,8,6,2,5,4,8,3,7]
f_m = height[0]
global_max_area = f_m
x1 = 0
for i in range(1 ,len(height)):

    if len(height) ==1:  #given n is atleast 2
        print(f_m)
        break

    if height[i] > f_m:
        s_m = f_m
        x2 = x1
        f_m = height[i]
        x1 = i
        print("i: ", i,"fm: ", f_m,"sm: ", s_m, "x1: ", x1,"x2: ", x2)

    elif height[i] > s_m:
        s_m = height[i]
        x2 = i
        print("i: ", i,"fm: ", f_m,"sm: ", s_m, "x1: ", x1,"x2: ", x2)

    local_max_area = f_m * (abs(x1 -x2))

    if local_max_area > global_max_area:
        global_max_area = local_max_area
        print("global_max ", global_max_area)

print(global_max_area)

################################################################################################################################################################################################
#%% second try with no help

height = [1,8,6,2,5,4,8,3,7]


#def max_Area(height):
height= [1,2,1]
    f_m = height[0]
    x1 = 0
    g_a = []

    for i in range(1, len(height)):

        # if len(height) ==1:  #given n is atleast 2
        # return f_m

        if height[i] >= f_m:
            s_m = f_m
            x2 = x1
            x1 = i
            g_a.append(min(f_m, s_m) * abs(x1 - x2))
            print("i: ",i,"g_a:",g_a)
            f_m = height[i]
            g_a.append(min(f_m, s_m) * abs(x1 - x2))
            print("i: ", i, "g_a:",g_a)
        else:
            s_m = height[i]
            x2 = i
            g_a.append(min(f_m, s_m) * abs(x1 - x2))
            print("i: ", i, "g_a:", g_a)

    print(max(g_a))

# test cases
height = [1,8,6,2,5,4,8,3,7]


print(max_Area([2,1]))

################################################################################################################################################################################################


#%%
### third try -

height= [1,2,1]
    f_m = []
    f_m.append(height[0])
    s_m = []
    x1 = 0
    g_a = []
    for i in range(1, len(height)):
        # if len(height) ==1:  #given n is atleast 2
        # return f_m
        max_fm = max(f_m)
        if height[i] >= max_fm:
            s_m.append(max_fm)
            max_sm = max(s_m)
            x2 = x1
            x1 = i
            print("i: ",i,"f_m: ", max_fm, "s_m:", max_sm)
            g_a.append(min(max_fm, max_sm) * abs(x1 - x2))
            print("i: ",i,"g_a:",g_a)
            f_m.append(height[i])
            max_fm = max(f_m)
            print("f_m: ", max_fm, "s_m:", max_sm)
            g_a.append(min(max_fm, max_sm) * abs(x1 - x2))
            print("i: ", i, "g_a:",g_a)
        else:
            s_m.append(height[i])
            x2 = i
            max_sm = max(s_m)
            print("i= ",i,"f_m: ",max_fm,"s_m:",max_sm, "x1:",x1,"x2:",x2)
            g_a.append(min(max_fm, max_sm) * abs(x1 - x2))
            print("i: ", i, "g_a:", g_a)
    print(max(g_a))



