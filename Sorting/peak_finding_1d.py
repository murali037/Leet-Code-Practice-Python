import numpy as np

x = [2,3,6,2,5,12,4,56,74,12,4,3,7]
def peak_finder(x):
    if type(x) is np.ndarray:
        x = np.array(x)

    if len(x) == 0:
        return None

    if len(x) == 2:
        print("len2: ", x[1])
        return x[1]

    k = len(x)//2
    print("k: ", x[k])

    if x[k] <= x[k-1]:
        print("left")
        peak = peak_finder(x[0:k])
        if peak:
            print("left peak: ", peak)
            return peak

    if x[k] <= x[k+1]:
        print("right")
        peak = peak_finder(x[k+1:len(x)])
        if peak:
            print("right peak: ", peak)
            return peak

    if x[k] > x[k-1] and x[k] > x[k+1]:
        return x[k]



x = [2,3,6,2,5,12,4,56,74,12,4,3,7]
peak_finder(x)
find_a_peak(x)


def find_a_peak(array):

    if type(x) is np.ndarray:
        array = np.array(array)

    if len(array) == 0:
        return None

    if len(array) == 2:
        print("len2: ", array[1])
        return array[1]

    half = len(array) // 2
    print("half: ", array[half])

    if array[half-1] < array[half] and array[half] > array[half+1]:
        print("middle peak: ", array[half])
        return array[half]

    if half >= 1 and array[half+1] >= array[half]:
        print("right")
        peak = find_a_peak(array[half:len(array)])
        if peak:
            print("right peak: ", peak)
            return peak

    if array[half-1] >= array[half]:
        print("left")
        peak = find_a_peak(array[0:half])
        if peak:
            print("left peak: ", peak)
            return peak

#%%
x
c= 2
if type(x) is np.ndarray:
    print("yes")
else:
    print("no")

print(c)