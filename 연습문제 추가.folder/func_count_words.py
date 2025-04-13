# func_count_words.py

def count_words(sentence):
    words = sentence.split()  # 공백을 기준으로 문자열 분리
    return len(words)  # 단어 수 반환

# 테스트 코드
sentence = "This is a test sentence"
word_count = count_words(sentence)

print(f"단어 수: {word_count}")