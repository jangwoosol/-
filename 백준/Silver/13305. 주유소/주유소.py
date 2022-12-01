n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=b[0]
cnt=0
for i in range(n-1):
    if m>b[i]:
        m=b[i]
    cnt+=m*a[i]
print(cnt)