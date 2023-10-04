class StringCalculator:
    def calculate(self, expression):
        try:
            num_tempo = ''      # 숫자를 임시로 저장
            result = 0          # 결과 값 저장
            operator = '+'      # 연산자 저장

            for char in expression:
                if char in '0123456789.':
                    num_tempo += char       # 숫자일 경우 추가
                else:
                    if num_tempo:
                        num = float(num_tempo)  # 문자 값을 실수형으로 변환
                        if operator == '+':
                            result += num
                        elif operator == '-':
                            result -= num
                        elif operator == '*':
                            result *= num
                        elif operator == '/':
                            result /= num
                        else:
                            raise ValueError("올바른 연산자가 아닙니다.")
                        num_tempo = ''      # num_tempo 초기화
                    if char in '+-*/':
                        operator = char     # 연산자 업데이트

            if num_tempo:
                num = float(num_tempo)      # 남은 숫자 계산
                if operator == '+':
                    result += num
                elif operator == '-':
                    result -= num
                elif operator == '*':
                    result *= num
                elif operator == '/':
                    result /= num

            return result
        except Exception as e:
            return f"올바른 연산식이 아닙니다: {str(e)}"

if __name__ == "__main__":
    calculator = StringCalculator()

    while True:
        expression = input("수식을 입력하세요 : ")
        #
        # if expression == 'exit':
        #     break

        result = calculator.calculate(expression)
        print(f"결과: {result}")
