# 사용자로부터 수식을 입력 받습니다.
expression = input("수식을 입력하세요: ")

try:
    # 입력된 수식을 계산하여 결과를 출력합니다.
    result = eval(expression)
    print("결과:", result)
except Exception as e:
    print("오류 발생:", e)