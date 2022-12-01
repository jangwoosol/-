a=input().split('-')
num=[]
for i in a:
  s=i.split('+')
  cnt=0
  for j in s:
    cnt+=int(j)
  num.append(cnt)
first=num[0]
for i in range(1,len(num)):
  first-=num[i]
print(first)