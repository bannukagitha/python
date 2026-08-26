def fib(n):
  if n<=1:
    return n
  
  return fib(n-1)+fib(n-2)
print(fib(5))
for i in range(6):
  print(fib(i),end=" ")