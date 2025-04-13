# for_sum.py

total_sum = 0

for number in range(1, 101):
    if number % 3 == 0:
        total_sum += number

print(f"3의 배수의 합: {total_sum}")