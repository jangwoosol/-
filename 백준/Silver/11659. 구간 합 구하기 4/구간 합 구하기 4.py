import sys
input=sys.stdin.readline

a,b=map(int,input().split())
k=list(map(int,input().split()))
summ=[0]

c=0
for i in k:
    c+=i
    summ.append(c)
    
for i in range(b):
    d,e =map(int,input().split())
    print(summ[e]-summ[d-1])