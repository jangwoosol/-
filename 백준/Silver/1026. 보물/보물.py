a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
b.sort()
c.sort(reverse=True)
cnt=0
for i in range(a):
  cnt+=b[i]*c[i]
print(cnt)