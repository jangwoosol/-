n=int(input())
a=[]
for i in range(n):
  a.append(list(input().split()))
a.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in a:
  print(i[0])