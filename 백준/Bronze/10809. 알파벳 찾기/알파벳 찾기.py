a=input()
alpha='abcdefghijklmnopqrstuvwxyz'
for i in alpha:
  if i in a:
    print(a.index(i), end=' ')
  else:
    print(-1,end=' ')