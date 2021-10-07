from robot import Robot

class Fleet:
    def __init__(self):
        self.robot_fleet = []

    def create_fleet(self):
        robo_one = Robot('Scrappy', 1500, 100)        
        robo_two = Robot('Spare parts', 2000, 150)
        robo_three = Robot('Shiny', 1800, 190)       
        self.robot_fleet.append(robo_one)
        self.robot_fleet.append(robo_two)
        self.robot_fleet.append(robo_three)


       