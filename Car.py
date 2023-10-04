import random

class Car:
    def __init__(self, name):
        self.name = name    # 자동차 이름 초기화
        self.position = 0   # 자동차 위치 초기화

    def move(self):
        if random.randint(0, 9) >= 4:
            self.position += 1      # 4 이상 뜨면 1보 전진

    def get_position(self):
        return self.position    # 현재 자동차 위치 반환

    def __str__(self):
        return f"{self.name} : {'-' * self.position}"   # 자동차 상태 문자열 반환

def main():
    try:
        car_names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분)\n").split(',')
        num_attempts = int(input("몇 회 시도하시겠습니까?\n"))
    except ValueError:      # int 값 안 넣으면 종료
        print("[ERROR] 올바른 값을 입력하세요.")
        return

    cars = [Car(_name.strip()) for _name in car_names]      # 입력받은 자동차 이름을 공백 제거하여 리스트로 저장

    print("\n실행 결과")
    for attempt in range(1, num_attempts + 1):
        print(f"\n{attempt}회차 경주 결과:")
        for _car in cars:
            _car.move()     # 각 자동차를 무작위로 이동시키고 결과 출력
            print(_car)

    max_position = max(_car.get_position() for _car in cars)        # 가장 멀리 이동한 자동차의 위치 찾기
    winners = [_car.name for _car in cars if _car.get_position() == max_position]       # 최종 우승자 찾기

    if len(winners) > 1:
        print(f"\n최종 우승자 : {','.join(winners)}")    # 구분자 쉼표로
    else:
        print(f"\n최종 우승자 : {winners[0]}")

if __name__ == "__main__":
    main()