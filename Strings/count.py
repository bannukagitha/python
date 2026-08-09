text=input()
vowels=0
consonants=0
digits=0
special=0
for ch in text:
  if ch in "aeiouAEIOU":
    vowels+=1
  elif ch.isalpha():
    consonants+=1
  elif ch.isdigit():
    digits+=1
  elif not ch.isalnum() and not ch.isspace():
    special+=1
print(vowels,consonants,digits,special)