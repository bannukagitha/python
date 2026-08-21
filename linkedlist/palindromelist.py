def isPalindrome(head):
  if not head:
      return False
  stack=[]
  temp=head
  while temp:
      stack.append(temp.val)
      temp=temp.next
  temp=head
  while temp:
      if temp.val!=stack.pop():
          return False
      temp=temp.next
  return True