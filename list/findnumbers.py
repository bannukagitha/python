def findNumbers(self, nums):
  even=0
  for num in nums:
      count=0
      while num>0:
          num//=10
          count+=1
      if count%2==0:
          even+=1
  return even 