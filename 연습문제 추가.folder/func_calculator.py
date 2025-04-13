def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"

# 테스트 코드
numbers = [1, 2, 3, 4, 5]
squares = [calculator(num, num, '*') for num in numbers]

print(squares)