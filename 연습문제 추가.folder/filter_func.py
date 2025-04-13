# filter_func.py

numbers = [10, 20, 30, 40, 50]

# 30보다 큰 수만 필터링
filtered_numbers = list(filter(lambda x: x > 30, numbers))

print(filtered_numbers)