n = int(input())

dp = [i for i in range(n + 1)] # 연산 최소 구하기 위한 dp
dp[1] = 0
history = [i for i in range(n + 1)] # 과정 저장
history[1] = 0

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1 # 이전 경우의 수로부터 +1이 되기 때문에 더함
    history[i] = i - 1
    #3되면 나누기
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        history[i] = i // 3
    # 2되면 나누기
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        history[i] = i // 2

print(dp[n])
print(n, end=" ")

while history[n] != 0:
    print(history[n], end=" ") # 역으로 출력
    n = history[n]