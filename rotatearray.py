class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        arr[:d] = reversed(arr[:d])
        arr[d:] = reversed(arr[d:])
        arr.reverse()
def main():
    arr = [1, 2, 3, 4, 5]
    d = 2
    obj = Solution()
    obj.rotateArr(arr, d)
    print("Rotated array is:", arr)
if __name__ == "__main__":
    main()