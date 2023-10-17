class GameView:
    @staticmethod
    def get_user_input():
        try:
            car_names = input("경주할 자동차 이름을 입력하세요. (이름은 쉼표(,) 기준으로 구분)\n").split(',')
            num_attempts = int(input("몇 회 시도하시겠습니까?\n"))
            if num_attempts < 0:
                raise MinusError("시도 횟수는 음수일 수 없습니다 (IllegalArgumentException).")
            return car_names, num_attempts
        except ValueError:
            print("[ERROR] 올바른 값을 입력하세요.")
            return None, None
        except MinusError as e:
            print(f"[ERROR] {e}")
            return None, None

    @staticmethod
    def display_winners(winners):
        if len(winners) > 1:
            print(f"\n최종 우승자 : {', '.join(winners)}")
        else:
            print(f"\n최종 우승자 : {winners[0]}")