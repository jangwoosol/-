data=input()
a=list(map(int,input().split()))
a.sort()
b=[]
count=0
for i in a:
  count+=i
  b.append(count)
print(sum(b))