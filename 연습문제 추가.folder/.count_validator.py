text = "Python is awesome"
vowels = "aeiouAEIOU"  # 대소문자 구분 없이 처리

count = 0
for char in text:
    if char in vowels:
        count += 1

print(f"모음 개수 : {count}")