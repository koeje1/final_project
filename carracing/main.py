from controller import GameController
from view import GameView

def main():
    car_names, num_attempts = GameView.get_user_input()
    if car_names is None:
        return

    game_controller = GameController()
    game_controller.create_cars(car_names)
    game_controller.race(num_attempts)
    winners = game_controller.find_winners()
    GameView.display_winners(winners)

if __name__ == "__main__":
    main()