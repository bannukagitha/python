class majorityElement:
    def majorityElement(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        n=len(nums)//2
        for x in freq:
            if freq[x] > n:
                return x
        return -1
def main():
    nums = [3, 2, 3]
    obj = majorityElement()
    result = obj.majorityElement(nums)
    print("Majority element is:", result)
if __name__ == "__main__":
    main()