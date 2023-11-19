from itertools import permutations

n = int(input())
num = list(permutations(list(range(1,10)), 3)) 
for _ in range(n):
    test, a, b = map(int, input().split())
    test = list(str(test))
    delete = 0

    for i in range(len(num)):
        a_cnt = b_cnt = 0 #스크라이크, 볼 둘다 아닐 때
        i -= delete

        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num[i]:
                if j == num[i].index(test[j]): #위치까지 같으면
                    a_cnt += 1 #스트라이크
                else:
                    b_cnt += 1 #볼
    
        if a_cnt != a or b_cnt != b:
            num.remove(num[i])
            delete += 1

print(len(num))