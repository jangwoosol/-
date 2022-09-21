a = int(input())
b = list(map(int, input().split()))
sum = [b[0]]
for i in range(len(b) - 1):
    sum.append(max(sum[i] + b[i + 1], b[i + 1]))
print(max(sum))