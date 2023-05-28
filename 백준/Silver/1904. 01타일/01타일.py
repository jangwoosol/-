import sys

N = int(sys.stdin.readline())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746 # (너무 큰 출력으로 인해) 나눠줌

print(dp[N])