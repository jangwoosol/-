# 이진탐색 구현 재귀함수
def binary_search(array,target, start, end):
	if start>end: # 탐색하는 범위에 데이터가 존재하지 않을 때
		return None
	mid =(start+end)//2
	if array[mid] == target:
		return mid
	elif array[mid] > target:
	# 중간점 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
		return binary_search(array, target, start, mid-1)
	else: # 클 경우
		return binary_search(array, target,mid+1, end)

n, target=list(map(int,input().split()))
# 전체원소 입력 받기
array=list(map(int,input().split()))

# 이진탐색 수행 결과 출력
result=binary_search(array,target, 0,n-1)
if result ==None:
	print('원소없음')
else:
	print(result+1) # 인덱스값 나오기때문에 1더해서 몇번째에 있나 출력

# 이진탐색 구현 반복문
def binary_search(array, target, start, end):
	while start<=end:
		mid=(start+end)//2
		if array[mid]==target:
			return mid
		elif array[mid]>target:
			end=mid-1
		else:
			start=mid+1
	return None
