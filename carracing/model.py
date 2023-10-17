import random

class Car:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        if random.randint(0, 9) >= 4:
            self.position += 1

    def get_position(self):
        return self.position

    def __str__(self):
        return f"{self.name} : {'-' * self.position}"