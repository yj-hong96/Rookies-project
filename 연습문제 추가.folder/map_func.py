# map_func.py

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# map 함수를 사용하여 두 리스트의 요소를 더한 새 리스트 생성
result = list(map(lambda x, y: x + y, list1, list2))

print(result)