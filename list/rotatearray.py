def rotateLeft(d, arr):
    d=d%len(arr)
    arr[:d] = reversed(arr[:d])
    arr[d:] = reversed(arr[d:])
    arr.reverse()
    return arr
arr=[1,2,3,4,5]
d=int(input())
print(rotateLeft(d,arr))