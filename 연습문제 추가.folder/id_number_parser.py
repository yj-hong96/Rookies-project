id_number = "960101-1234567"

birth = id_number[:6]
century_code = id_number[7]

if century_code in ['1', '2']:
    year_prefix = "19"
elif century_code in ['3','4']:
    year_prefix = "20"
else:
    year_prefix = ""


year_prefix + birth[0:2]
mnonth = birth[2:4]
day = birth[4:6]

print(f"{year}년 {mnonth}월 {day}일")
