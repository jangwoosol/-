def fact(n):
    num=1
    for i in range(1,n+1):
        num*= i
    return num

a=int(input())
for i in range(a):
    n, m=map(int,input().split())
    k=fact(m)//(fact(n)*fact(m-n))
    print(k)