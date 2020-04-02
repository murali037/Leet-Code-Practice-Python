#%%

height = [0,1,0,2,1,0,1,3,2,1,2,1]

x = 0
y = len(height) - 1
rain_vol = 0
fl = height[x]
sl = height[y]

while x != y:
    print("x", x, "y", y)
    if (fl == 0 and x == 0):
        x += 1
        fl = height[x]

    if (sl == 0 and y == len(height) - 1):
        y -= 1
        sl = height[y]

    if rain_vol == 0:
        print("fl:",fl, "sl:", sl, x, y)
        rain_ht = min(fl, sl)
        rain_vol += rain_ht * (y - x-1)
        print("vol:",rain_vol)

    if x != y:
        x += 1
        fl = height[x]
        if height[x] == 0:
            rain_vol = rain_vol
        elif height[x] > rain_ht:
            rain_vol -= rain_ht
            rain_ht = min(fl, sl)
            rain_vol += rain_ht * (y - x - 1)
            print("left: ", rain_vol, "fl: ", fl, "sl: ", sl, "ht", rain_ht)
        else:
            rain_vol += rain_ht - height[x]
            rain_ht = min(fl, sl)
            rain_vol += rain_ht * (y - x - 1)
            print("left: ", rain_vol, "fl: ", fl, "sl: ", sl, "ht", rain_ht)



    if x != y:
        y -= 1
        sl = height[y]
        if height[y] == 0:
            rain_vol = rain_vol
        elif height[y] > rain_ht:
            rain_vol -= rain_ht
        else:
            rain_vol += rain_ht - height[y]

    rain_ht = min(fl, sl)
    rain_vol += rain_ht * (y - x-1)
    print("right: ", rain_vol, "fl: ", fl, "sl: ", sl, "ht", rain_ht)

print(rain_vol)
