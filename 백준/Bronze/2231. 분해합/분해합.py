target = int(input())
 
for i in range(target):
    temp = sum(map(int, str(i))) # 각 자릿수의 합 10이면 1, 11이면 2
    result = i + temp # i값과 더함 11이면 11+2 =13
    if result == target:
        print(i)
        break
else:
    print(0)