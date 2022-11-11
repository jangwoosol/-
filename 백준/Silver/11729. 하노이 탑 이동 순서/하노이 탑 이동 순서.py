n=int(input())
#a는 현재 n개의 원판이 쌓여있는 곳, b는 n-1개의 원판을 옮겨 놓을 곳, C는 a에서 남은 원판을 놓을 곳
def hano(n,a,b,c): 
    if n==1:
        print(a,c)
    else:
        hano(n-1,a,c,b)
        print(a,c)
        hano(n-1,b,a,c)
cnt=0
for i in range(n):
    cnt=2*cnt+1 
print(cnt)
hano(n,1,2,3)