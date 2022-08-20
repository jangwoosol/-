n = int(input())
data = list(map(int, input().split()))
count = 0

for x in data:
  for i in range(2, x+1): #1은 소수 아님
    if x % i == 0:
      if x == i:
        count += 1
      
      break

print(count)