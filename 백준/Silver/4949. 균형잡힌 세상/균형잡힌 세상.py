while True:
    s=input()
    if s=='.':
        break
    k=[]
    temp=True
    for i in s:
        if i=='(' or i=='[':
            k.append(i)
        elif i==')':
            if not k or k[-1]=='[':
                temp=False
                break
            elif k[-1]=='(':
                k.pop()
        elif i == ']':
            if not k or k[-1] == '(':
                temp = False
                break
            elif k[-1] == '[':
                k.pop()
    if temp == True and not k:
        print('yes')
    else:
        print('no')