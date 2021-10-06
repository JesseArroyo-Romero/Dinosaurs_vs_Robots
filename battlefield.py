from herd import Herd
from fleet import Fleet
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot_fleet = Fleet()
        print(self.robot_fleet)
        self.dino_herd = Herd()


    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()


    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs!')


    def battle(self):
        self.dino_turn('Velociraptor')
        self.dino_turn('T-Rex')
        self.dino_turn('Terrordactyl')
        self.robo_turn('Scrappy')
        self.robo_turn('Spare parts')
        self.robo_turn('Shiny')

    
    def dino_turn(self, dinosaur):
        attack = self.dino_herd.attack(self.robot_fleet)
        command = input('Attack robot fleet? yes or no? ')
        if command == 'yes':
            attack
        elif command == 'no':
            pass


    def robo_turn(self, robot):
        command = input('Attack dino herd? yes or no? ')
        if command == 'yes':
            pass

        elif command =='no':
            pass


    def show_dino_opponent_options(self):
        pass


    def show_robo_opponent_options(self):
        pass


    def display_winners(self):
        if self.fleet == 0:
            print('The robots have won!')
            
        elif self.herd == 0:
            print('The dinos have won!')

            
