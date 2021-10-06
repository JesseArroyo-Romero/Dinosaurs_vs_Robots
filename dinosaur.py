from robot import Robot

class Dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        

    def attack(self, robot):
        self.attack_power - robot


    def __str__(self):
        return self.name