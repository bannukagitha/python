def countDigits(self, n):
  # code here
  if n==0:
      return 0
  return 1+self.countDigits(n//10)