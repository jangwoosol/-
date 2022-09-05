#2750번과 문제는 같지만 속도 차이로 sys.stdin.readline() 사용하여 속도문제 해결
#input() 내장 함수는 parameter로 prompt message를 받을 수 있다. 따라서 입력받기 전 prompt message를 출력해야 한다
#sys.stdin.readline()은 prompt message를 인수로 받지 않는다. 또한, input() 내장 함수는 입력받은 값의 개행 문자를 삭제시켜서 리턴한다.

import sys

n = int(input())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
    print(i)