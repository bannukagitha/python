text=input()
freq={}
for ch in text:
  freq[ch]=freq.get(ch,0)+1
print(freq)
max_char=max(freq,key=freq.get)
print(f"Maximun repeating character:{max_char}")
for ch in freq:
  if freq[ch]==1:
    print(f"first non repeating character:{ch}")
    break
else:
  print("NO repeating characters")
for ch in freq:
  if freq[ch]>1:
      print(f"frist repeating charecter:{ch}")
      break
else:
  print("NO repeating characters")
