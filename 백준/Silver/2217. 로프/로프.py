a=int(input())
c=[]
for i in range(a):
  c.append(int(input()))
c.sort(reverse=True)
m=[]
for i in range(len(c)):
  m.append((i+1)*c[i])
print(max(m))