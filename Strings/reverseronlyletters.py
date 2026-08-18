def reverseOnlyLetters(s):
  new=list(s)
  left,right=0,len(new)-1
  while left < right:
      if new[left].isalpha() and new[right].isalpha():
          new[left],new[right]=new[right],new[left]
          left+=1
          right-=1
      if not new[right].isalpha():
          right-=1
      if not new[left].isalpha():
          left+=1
  return "".join(new)