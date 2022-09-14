import sys

a = list(map(str, sys.stdin.readline().rstrip("\n")))

s = set() # set 자료 구조를 통해 중복을 제거

# 반복문을 통해 부분 문자열을 찾는다.
for i in range(len(a)):
    for j in range(len(a) + 1):
        # 부분 문자열이 있으면 s에 저장
        if a[i:j]:
            s.add("".join(a[i:j]))

# s의 길이를 출력 = 개수 출력
print(len(s))