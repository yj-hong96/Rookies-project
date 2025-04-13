# bmi_calculator.py

# 사용자 입력 받기
weight = float(input("체중(kg): "))
height_cm = float(input("키(cm): "))

# 키 단위를 cm → m로 변환
height_m = height_cm / 100

# BMI 계산
bmi = weight / (height_m ** 2)

# 결과 출력
print(f"\n계산된 BMI: {bmi:.2f}")

# BMI 범위 해석
if bmi < 18.5:
    print("저체중입니다.")
elif 18.5 <= bmi < 23:
    print("정상 체중입니다.")
elif 23 <= bmi < 25:
    print("과체중입니다.")
else:
    print("비만입니다.")
