# time_converter.py

total_seconds = 12345

# 시 계산
hours = total_seconds // 3600
# 남은 초 계산
remaining_seconds = total_seconds % 3600
# 분 계산
minutes = remaining_seconds // 60
# 초 계산
seconds = remaining_seconds % 60

# 결과 출력
print(f"{total_seconds}초는 {hours}시간 {minutes}분 {seconds}초입니다.")