import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))
#가지고 있는 cards를 모두 dict에 0(아무 숫자로 가능)로 등록(mapping)
dict = {} 
for i in range(len(cards)):
    dict[cards[i]] = 0 

for j in range(M):
    if checks[j] not in dict:
        print(0, end=' ')
    else:
        print(1, end=' ')