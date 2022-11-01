n=1260
count=0
arr=[500,100,50,10] # 큰 단위부터 차례대로 확인하기
for i in arr:
		count+=n//i # 동전 개수 세기
		n%= i # 동전으로 원래돈을 나눈나머지로 계속해서 계산
print(count)
