## 방법1 : 이분탐색법

from sys import stdin
_ = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
M = map(int,stdin.readline().split())

# n != 중간요소 인 경우 : 탐색 범위를 절반으로 나눈 후 이분 탐색을 계속해서 진행
# n == 중간요소인 경우 : start에서 end까지의 범위에서 count() 메소드를 사용해서 몇 개가 있는지를 센 후 return
def binary(n, N, start, end): 
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:  #N의 요소인 n을 중간 값과 비교한다.
        return N[start:end+1].count(n)
    elif n < N[m]: 
        return binary(n, N, start, m-1)
    else:
        return binary(n, N, m+1, end)

n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))

## 방법2 : Counter 사용
from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

# 리스트 N을 Counter에 넣으면 N의 요소들의 숫자를 센 Dictionary자료형이 출력
C = Counter(N) 
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))
