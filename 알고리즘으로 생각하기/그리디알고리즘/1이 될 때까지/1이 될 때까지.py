n,k=map(int, input().split())
result=0
while True:
  # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
  target=(n//k)*k
  result+=(n-target) #1을 빼는 연산 횟수
  n=target
  # n이 k보다 작을 때 더이상 나눌 수 없으니 반복문 탈출 
  if n<k:
    break
  # k로 나누기 (// 연산기호: 나머지 소숫점 이하 버리는 나누기)
  n//=k
  result+=1 # 나눠지는 연산 개수 하나씩 추가
  print(result)
# 마지막 남은 수에 대해 1씩 빼서 횟수 더하기
result+=(n-1)
print(result)
