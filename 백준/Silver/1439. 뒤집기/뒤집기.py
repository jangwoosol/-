n=input()
cnt=0
for i in range(len(n)-1): #i+1과 비교해줄 것으로 -1해야한다.
    if n[i]!=n[i+1]:
        cnt+=1
print((cnt+1)//2) 
# 0 또는 1 중하나로만 바꾸면 되기에 //2 나누기 2만 해주면 된다.