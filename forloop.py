n=int(input())
total=(n*(n+1))//2
print(total)
fact=1
for i in range(1,n+1):
    print(n,"*",i,"=",n*i)
    fact*=i
print(fact)
prime=True
if n <= 1:
    prime=False
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        prime=False
    prime=True
print("prime:",prime)
temp=n
res=0
su=0
while temp>0:
    digit=temp%10
    res=(res*10)+digit
    su+=digit
    temp//=10
print("palindrome"if n==res else "not")
print(res,su,sep="\n")
a, b = 0, 1
count1 = 0

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(a)
else:
    while count1 < n:
        print(a, end=" ")
        a, b = b, a + b
        count1 += 1
digits = len(str(n))
total1 = 0

while temp > 0:
    degit = temp % 10
    total += degit ** digits
    temp //= 10

if total1 == n:
    print("Armstrong")
else:
    print("Not Armstrong")
