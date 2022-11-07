n=int(input())
data=list(map(int, input().split()))
data.sort()
result=0 # 총 그룹 수
count=0 # 현재 그룹에 포함된 모함가 수
for i in data: # 공포도 낮은 것부터하나씩 확인
  count+=1 # 현재 그룹에 해당 모함가 포함시키기
  if count>=i: # 해당그룹에 포함된 모험가 수가 현재 공포도 이상이라면, 그룹 결성
    result+=1 # 총그룹의 수도 증가시키기
    count=0 # 현재 그룹에 포함된 모험가 수 초기화
  print(result, count)
print(result)
