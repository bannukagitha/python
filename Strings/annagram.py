n,m=input().split()
if len(n)!=len(m):
  print("NO")
else:
  freq={}
  for ch in n:
    freq[ch]=freq.get(ch,0)+1
  for ch in m:
    if not ch in freq or freq[ch]==0:
      print("NO")
      break
    else:
      freq[ch]-=1
  else:
    print("YES")
