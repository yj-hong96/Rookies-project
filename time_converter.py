# time_converter.py

# 사용자에게 초 입력 받기
total_seconds = int(input("초를 입력하세요: "))

# 시, 분, 초 계산
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# 결과 출력
print(f"{total_seconds}초는 {hours}시간 {minutes}분 {seconds}초입니다.")
