def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else : 
        return 1

a, b=map(int, input().split())
result=1
for i in range(a-b+1, a+1,1):
    result*=i

print(int(result/factorial(b)))