text=input()
vowels=0
consonants=0
for ch in text:
  if ch in "aeiouAEIOU":
    vowels+=1
  else:
    consonants+=1
print(vowels,consonants)