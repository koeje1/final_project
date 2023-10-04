class WordRelayGame:
    def __init__(self):
        self.used_words = []    # 단어저장 리스트
        self.players = []   # 플레이어 이름저장 리스트
        self.scores = {}    # 플레이어 점수 저장 딕셔너리

    def get_player_names(self):
        num_players = int(input("참여할 플레이어의 수를 입력해 주세요: "))
        for i in range(num_players):
            player_name = input(f"플레이어의 이름을 입력해 주세요 플레이어{i+1}:\n")
            self.players.append(player_name)
            self.scores[player_name] = 5    # 초기값 5점 설정

    def is_korean_word(self, word):
        korean_range = (ord('가'), ord('힣'))  # 한글 유니코드 범위 (가 ~ 힣)
        return all(korean_range[0] <= ord(char) <= korean_range[1] for char in word)

    def start(self):
        print("끝말잇기 게임을 시작합니다.")
        self.get_player_names()
        print("시작하겠습니다.")
        print("""규칙
1. 게임에서 유저가 제출 할 수 있는 단어는 한글만 가능합니다.
- 특수문자, 영어, 숫자, 띄어쓰기 불가
2. 글자수는 10자 이하여야 합니다.
3. 한번 등장한 단어는 중첩해서 나올 수 없습니다.
4. 규칙을 어기시면 상대편 턴으로 넘어갑니다.
""")
        previous_word = None    # 단어 저장
        current_player_index = 0    # 플레이어 인덱스 저장

        while True:
            current_player = self.players[current_player_index]
            if self.scores[current_player] <= 0:
                print(f"{current_player} 점수가 0 이하입니다. 게임을 종료합니다.")
                return

            input_word = input(f"플레이어 [{current_player}], 단어를 입력해 주세요 [현재점수 {self.scores[current_player]}]: ")

            if input_word == "ㅈㅈ":
                reconfirm = input("정말로 게임을 포기하시겠습니까? [확인 1]: ")
                if reconfirm == '1':
                    print(f"Game over. 플레이어 [{current_player}]님이 기권하셨습니다.")
                    return
                else:
                    print("올바른 선택이 아닙니다.")
                    continue

            if not self.is_korean_word(input_word):
                print("한글만 입력 가능합니다. [규칙 1 위배]")
                if previous_word is not None:
                    self.scores[current_player] -= 1
                continue

            elif len(input_word) >= 10:
                print("10자 미만의 단어를 입력해 주세요. [규칙 2 위배]")
                if previous_word is not None:
                    self.scores[current_player] -= 1
                continue
            elif input_word in self.used_words:
                print("중첩 된 단어는 쓰실 수 없습니다. [규칙 3 위배]")
                if previous_word is not None:
                    self.scores[current_player] -= 1
                continue

            if previous_word is None:   # 플레이어 첫턴
                previous_word = input_word
            elif input_word[0] == previous_word[-1]:
                self.used_words.append(input_word)
                previous_word = input_word
                print(f"현재 단어: {input_word}")

                # 올바른 단어를 입력하면 1점 증가
                self.scores[current_player] += 1
                print(f"플레이어 [{current_player}]의 점수: {self.scores[current_player]}")
            else:
                print("끝말있기 룰에 어긋납니다.")
                self.scores[current_player] -= 1

            # 다음 플레이어로 넘어가기 위해 나머지 처리
            current_player_index = (current_player_index + 1) % len(self.players)


if __name__ == "__main__":
    game = WordRelayGame()
    game.start()