n, m = list(map(int, input().split()))
a=[]
for i in range(n):
  k=int(input())
  a.append(k)
start=1
end=max(a)
while start<=end:
  mid=(start+end)//2
  total=0
  for i in a:
    total+=i//mid
  if total < m:
      end = mid - 1 
  else:
      start = mid + 1
print(end)