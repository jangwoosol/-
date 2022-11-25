a=int(input())
b=[]
for i in range(a):
    b.append(input())
b=set(b)# 중복제거
b=list(b)
b.sort()
b.sort(key=lambda x: len(x))

for i in b:
    print(i)