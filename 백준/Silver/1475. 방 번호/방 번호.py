n = input()
cnt = [0] * 9
for i in n:
    k=int(i)
    if k==9:
        k=6
    cnt[k]+=1
cnt[6]=(cnt[6]+1)//2 #9도 6으로 취급해서 넣었으니 개수 셀 때 반 나눔!
print(max(cnt))
