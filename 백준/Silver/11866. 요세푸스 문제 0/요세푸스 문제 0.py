n,k=list(map(int,input().split()))
num=list(range(1,n+1))
cnt=0
answer=[] 
for i in range(n):
    cnt+=k-1
    if cnt>=len(num):
        cnt=cnt%len(num) #한바퀴 돌고 그 다음 돌아올 때 대비해 값을 나머지로 바꿈
    answer.append(str(num.pop(cnt)))
print("<",", ".join(answer),">",sep="")