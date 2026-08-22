def checkDivisibility(n):
  temp=n
  total=0
  product=1
  while temp>0:
      digit=temp%10
      total+=digit
      product*=digit
      temp//=10
  if n % (total+product) ==0:
      return True
  else:
      return False