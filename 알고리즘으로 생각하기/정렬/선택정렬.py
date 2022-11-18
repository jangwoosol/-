# 처리되지 않은 데이터 중 가장 작은 데이터를 선택 해 맨 앞에 있는 데이터와 바꾼다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]: #작은원소보다 더 작은게 있다면 
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프 : 위치바꿈

print(array)
