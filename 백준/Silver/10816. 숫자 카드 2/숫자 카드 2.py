from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
dic = {}
for n in N:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

print(' '.join(str(dic[i]) if i in dic else '0' for i in M))

''' code는 같지만 런타임에러
for i in M:
  if i in dic:
    print(' '.join(str(dic[i])),end=' ')
  else:
    print('0', end=' ') 
''' 
