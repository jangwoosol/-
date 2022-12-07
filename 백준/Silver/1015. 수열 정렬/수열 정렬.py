n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
k=[]
for i in a:
  k.append(b.index(i))
  b[b.index(i)]=-1 # 이미 할당된 숫자는 -1로 대체해 재탐색되지 않도록 한다. 같은 숫자인거 인덱스 바꿔줌
for i in k:
  print(i,end=' ')