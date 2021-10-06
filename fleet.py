from robot import Robot

class Fleet:
    def __init__(self):
        self.robo_one = Robot('Scrappy', 1500, 100)        
        self.robo_two = Robot('Spare parts', 2000, 150)
        self.robo_three = Robot('Shiny', 1800, 190)

    def create_fleet(self):
        self.robot_fleet = [self.robo_one, self.robo_two, self.robo_three]
