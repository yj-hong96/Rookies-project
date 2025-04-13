# 문자열 연결
greeting = "Hello" + " " + "World"
print(greeting)  # Hello World

# 대문자로 변환
upper_greeting = greeting.upper()
print(upper_greeting)  # HELLO WORLD

# "World"만 슬라이싱
world = greeting[6:]  # 인덱스 6부터 끝까지
print(world)  # World

# 문자열 분리
text = "Python is fun"
split_text = text.split()  # 공백 기준 분리
print(split_text)  # ['Python', 'is', 'fun']

# 짝수 인덱스 문자 출력
s = "abcdef"
even_index_chars = s[::2]  # 0, 2, 4 인덱스 문자
print(even_index_chars)  # ace

# "Hello" 3번 반복
repeat_hello = "Hello" * 3
print(repeat_hello)  # HelloHelloHello