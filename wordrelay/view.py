class WordRelayGameView:
    def show_welcome_message(self):
        print("끝말잇기 게임을 시작합니다.")

    def get_num_players(self):
        try:
            return int(input("참여할 플레이어의 수를 입력해 주세요: "))
        except ValueError:
            print("올바른 숫자를 입력해 주세요.")
            return self.get_num_players()

    def get_player_name(self, player_number):
        return input(f"플레이어의 이름을 입력해 주세요 플레이어{player_number}:\n")

    def show_game_rules(self):
        print("""규칙
1. 게임에서 유저가 제출 할 수 있는 단어는 한글만 가능합니다.
- 특수문자, 영어, 숫자, 띄어쓰기 불가
2. 글자수는 10자 이하여야 합니다.
3. 한번 등장한 단어는 중첩해서 나올 수 없습니다.
4. 규칙을 지키면 [+1점], 어기면 [-3점]입니다
5. 게임을 포기하시려면 ㅈㅈ 입력해주시면 됩니다.
        """)

    def show_current_word(self, word):
        print(f"현재 단어: {word}")

    def get_player_input(self, player_name, score):
        return input(f"플레이어 [{player_name}], 단어를 입력해 주세요 [현재점수 {score}]: ")

    def show_game_over(self, player_name):
        print(f"플레이어 [{player_name}] 점수가 0 이하입니다. 게임에 패배하셨습니다.")