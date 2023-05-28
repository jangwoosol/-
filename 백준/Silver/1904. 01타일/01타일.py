# 0 ->0 1->1 2->2 3-> 3 4-> 5 5->8
# 헉 이전 두개 값 더하는 거다. = 피보나치 수열
def fib(n):
  a,b=1,2
  
  for i in range(n-2):
    a,b=b%15746,(a+b)%15746
  return b

n=int(input())

if n==1:
  print(1)
else:
  print(fib((n)))