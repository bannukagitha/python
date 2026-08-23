def rotateRight( head, k):
  if not head or not head.next or k==0:
      return head
  temp=head
  length=1
  while temp.next:
      length+=1
      temp=temp.next
  k=k%length
  if k==0:
      return head
  temp.next=head
  new_tail=head
  for _ in range(length-k-1):
      new_tail=new_tail.next
  new_head=new_tail.next
  new_tail.next=None

  return new_head