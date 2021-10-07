class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        

    def attack(self, dinosaur):
        remaining_health = dinosaur.health - self.weapon
        return remaining_health


    def __str__(self):
        return self.name