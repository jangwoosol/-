# 원하는 숫자 나올 때까지 1번째 위치로 옮기기
#1번 방법으로 원소 뽑기
n,m=list(map(int,input().split()))
k=list(map(int,input().split()))
num=list(range(1,n+1))
cnt=0
for i in k:
    while True: #뽑을 때까지
        if num[0]==i:
            num.pop(0)
            break
        else:
            if num.index(i)<len(num)/2 : # 왼쪽에서 빼는게 더 빠를 때
                while num[0]!=i:
                    num.append(num.pop(0))
                    cnt+=1
            else:
                while num[0]!=i:
                    num.insert(0,num.pop())
                    cnt+=1
print(cnt)