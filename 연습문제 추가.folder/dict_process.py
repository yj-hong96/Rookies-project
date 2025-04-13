
# 1. "age"의 값을 출력
person = {"name": "John", "age": 30}
print(f"나이: {person['age']}")

# 2. 모든 과목명을 출력
subjects = {"math": 90, "science": 85, "history": 78}
print(f"과목들: {list(subjects.keys())}")

# 3. 'apple'의 값을 2 증가시킴
fruit_count = {'apple': 3, 'banana': 5}
fruit_count['apple'] += 2
print(fruit_count)

# 4. 리스트 오름차순 정렬
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)