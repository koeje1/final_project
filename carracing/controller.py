from model import Car

class GameController:
    def __init__(self):
        self.cars = []

    def create_cars(self, car_names):
        self.cars = [Car(_name.strip()) for _name in car_names]

    def race(self, num_attempts):
        for attempt in range(1, num_attempts + 1):
            print(f"\n{attempt}회차 경주 결과:")
            for _car in self.cars:
                _car.move()
                print(_car)

    def find_winners(self):
        max_position = max(_car.get_position() for _car in self.cars)
        winners = [_car.name for _car in self.cars if _car.get_position() == max_position]
        return winners