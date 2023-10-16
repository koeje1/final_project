import random

class WordRelayGame:
    def __init__(self):
        self.used_words = []
        self.players = []
        self.scores = {}
        self.current_player_index = 0

    @staticmethod
    def get_positive_input(prompt):
        while True:
            try:
                user_input = int(input(prompt))
                if user_input > 0:
                    return user_input
                else:
                    print("양수를 입력해 주세요.")
            except ValueError:
                print("올바른 숫자를 입력해 주세요.")

    def get_player_names(self):
        num_players = self.get_positive_input("참여할 플레이어의 수를 입력해 주세요: ")

        for i in range(num_players):
            player_name = input(f"플레이어의 이름을 입력해 주세요 플레이어{i + 1}:\n")
            self.players.append(player_name)
            self.scores[player_name] = 5

    def is_korean_word(self, word):
        return all(ord('가') <= ord(char) <= ord('힣') for char in word)

    def play_game(self, starting_word):
        previous_word = starting_word

        while True:
            current_player = self.players[self.current_player_index]
            if self.scores[current_player] <= 0:
                print(f"플레이어 [{current_player}] 점수가 0 이하입니다. 게임에 패배하셨습니다.")
                return

            input_word = input(f"플레이어 [{current_player}], 단어를 입력해 주세요 [현재점수 {self.scores[current_player]}]: ")

            if self.process_input_word(input_word, previous_word):
                self.used_words.append(input_word)
                previous_word = input_word
                self.current_player_index = (self.current_player_index + 1) % len(self.players)

    # def give_up_rule(self, current_player, input_word):
    #     if input_word == "ㅈㅈ":
    #         print(f"플레이어 [{current_player}]님이 게임을 종료하셨습니다.")
    #         exit()

    def give_up_rule(self, current_player, input_word):
        while True:
            if input_word == "ㅈㅈ":
                reconfirm = input("정말로 게임을 포기하시겠습니까? [확인 1]: ")
                if reconfirm == '1':
                    print(f"Game over. 플레이어 [{current_player}]님이 기권하셨습니다.")
                    exit()
                else:
                    print("올바른 선택이 아닙니다.")
                    input(f"플레이어 [{current_player}], 단어를 입력해 주세요 [현재점수 {self.scores[current_player]}]: ")
            else:
                return False

    def is_korean_word_rule(self, current_player, input_word):
        if not self.is_korean_word(input_word):
            print("한글만 입력 가능합니다. [규칙 1 위배]")
            self.scores[current_player] -= 3
            return False
        return True

    def length_rule(self, current_player, input_word):
        if len(input_word) >= 10 or len(input_word) < 2:
            print("2자 이상 10자 미만의 단어를 입력해 주세요. [규칙 2 위배]")
            self.scores[current_player] -= 3
            return False
        return True

    def nested_rule(self, current_player, input_word):
        if input_word in self.used_words:
            print("중첩 된 단어는 쓰실 수 없습니다. [규칙 3 위배]")
            self.scores[current_player] -= 3
            return False
        return True

    def relay_rule(self, current_player, input_word, previous_word):
        if input_word[0] != previous_word[-1]:
            print("끝말잇기 룰에 어긋납니다.")
            self.scores[current_player] -= 3
            return False
        return True

    def process_input_word(self, input_word, previous_word):
        current_player = self.players[self.current_player_index]

        if self.give_up_rule(current_player, input_word):
            return True

        if self.is_korean_word_rule(current_player, input_word) and \
                self.length_rule(current_player, input_word) and \
                self.nested_rule(current_player, input_word) and \
                self.relay_rule(current_player, input_word, previous_word):

            self.scores[current_player] += 1
            print(f"플레이어 [{current_player}]의 점수: {self.scores[current_player]}")
            return True
        else:
            return False

