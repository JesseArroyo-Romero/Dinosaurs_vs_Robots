
from robot import Robot
from fleet import Fleet


class Dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        

    def attack(self, robot):
        robot.health = robot.health - self.attack_power
        return robot.health

    def __str__(self):
        return self.name