text1,text2=input().split()
#if text1==text2[::-1]:
#    print("YES")
#:
#    print("NO")
if len(text1)!=len(text2):
    print("NO")
else:
    left=0
    right=len(text2)-1
    while left<right:
        if text1[left]!=text2[right]:
            print("NO")
            break
        left+=1
        right-=1
    else:
        print("YES")