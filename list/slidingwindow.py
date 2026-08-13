n,window_size=map(int,input().split())
arr=list(map(int,input().split()))
window_sum=sum(arr[:window_size])
max_window=window_sum
for i in range(window_size,n):
  window_sum+=arr[i]
  window_sum-=arr[i-window_size]
  max_window=max(max_window,window_sum)
print(max_window)