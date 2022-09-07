from collections import Counter
import sys

a=int(sys.stdin.readline())
b=[]
for i in range(a):
  k=int(sys.stdin.readline())
  b.append(k)
b.sort()
print(round(sum(b)/len(b)))
print(b[a//2])

cnt = Counter(b).most_common(2)

if len(b) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(b[-1]-b[0])