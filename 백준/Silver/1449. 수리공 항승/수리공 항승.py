n,l = map(int, input().split())
position=list(map(int, input().split()))
position.sort()
start=position[0]
end=position[0]+l
cnt=1
for i in range(n):
    if start<=position[i]<end:
        continue
    else:
        start=position[i]
        end=position[i]+l
        cnt+=1
print(cnt)