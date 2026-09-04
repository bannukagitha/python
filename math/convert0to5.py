def convertFive(self, n):
  if not n:
      return 5
  res=0
  i=1
  while n:
      digit=n%10
      if digit==0:
          res=(5*i)+res
      else:
          res=(digit*i)+res
      i*=10
      n//=10
  return res