# 합한값이 그 다음 값보다 클지, 작을지에 따라 결정할 수 있따.
a = int(input())
b = list(map(int, input().split()))
sum = [b[0]]
for i in range(len(b) - 1):
    sum.append(max(sum[i] + b[i + 1], b[i + 1]))
print(max(sum))
