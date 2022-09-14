# set을 이용하면 차집합을 구할 수 있다.
a, b= map(int,input().split())
al=set(map(int, input().split()))
bl=set(map(int, input().split()))
print(len(al-bl)+len(bl-al))