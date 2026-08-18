def finalString(s):
  new=[]
  for x in s:
      if x=="i":
          new=new[::-1]
      else:
          new.append(x)
  return "".join(new)