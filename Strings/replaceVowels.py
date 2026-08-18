def reverseVowels(s):
  Vowels="AEIOUaeiou"
  s=list(s)
  left=0
  right=len(s)-1
  while left <right:
      if s[left] in Vowels and s[right] in Vowels:
          s[left],s[right]=s[right],s[left]
          left+=1
          right-=1
      if s[left] not in Vowels:
          left+=1
      if s[right] not in Vowels:
          right-=1
  s="".join(s)
  return s