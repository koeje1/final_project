import random
from model import WordRelayGame
from view import WordRelayGameView

class WordRelayGameController:
    def __init__(self):
        self.model = WordRelayGame()
        self.view = WordRelayGameView()

    def run(self):
        self.view.show_welcome_message()
        num_players = self.view.get_num_players()

        for i in range(num_players):
            player_name = self.view.get_player_name(i + 1)
            self.model.players.append(player_name)
            self.model.scores[player_name] = 5

        self.view.show_game_rules()

        starting_words = ["가", "나", "다", "라", "마", "바", "사"]
        starting_word = random.choice(starting_words)
        self.view.show_current_word(starting_word)

        self.play_game(starting_word)

    def play_game(self, starting_word):
        previous_word = starting_word

        while True:
            current_player = self.model.players[self.model.current_player_index]
            if self.model.scores[current_player] <= 0:
                self.view.show_game_over(current_player)
                return

            input_word = self.view.get_player_input(current_player, self.model.scores[current_player])

            if self.model.process_input_word(input_word, previous_word):
                self.model.used_words.append(input_word)
                previous_word = input_word
                self.view.show_current_word(input_word)
                self.model.current_player_index = (self.model.current_player_index + 1) % len(self.model.players)
