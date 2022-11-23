a = int(input())
b=[]
for i in range(a):
  n= list(map(int, input().split()))
  b.append(n)
b.sort()
for i in b:
  print(i[0],i[1])