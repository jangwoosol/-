n=int(input())
a=list(map(int,input().split()))

target=1
stack=[]

while a:
    if target==a[0]:
        a.pop(0)
        target+=1
    else:
        stack.append(a.pop(0))
    while stack:
        if stack[-1]==target:
            stack.pop()
            target+=1
        else:
            break
if not stack:
    print('Nice')
else:
    print('Sad')
        