# list 보다 set, dict이 hash값을 사용하기 때문에 시간복잡성이 낮다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = set([input() for i in range(N)]) #dict 사용가능
cnt = 0
for i in range(M):
    t = input()
    if t in s:
        cnt += 1
print(cnt)