from herd import Herd
from fleet import Fleet
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.fleet.create_fleet()
        print(self.fleet.robot_fleet)
        self.herd = Herd()
        self.herd.create_herd()


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
        if dinosaur == 'Velociraptor':
            print('Look at Velociraptor go!')
            self.herd.dino_herd[0].attack(self.fleet.robot_fleet[0])
            print(f"Scrappy's health is: {self.fleet.robot_fleet[0].health}")

            if self.fleet.robot_fleet[0].health == 0 :
                print('Look at Velociraptor go!')
                self.herd.dino_herd[0].attack(self.fleet.robot_fleet[1])
                print(f"Spare parts health is: {self.fleet.robot_fleet[1].health}")

                if self.fleet.robot_fleet[1].health == 0 :
                    print('Look at Velociraptor go!')
                    self.herd.dino_herd[0].attack(self.fleet.robot_fleet[2])
                    print(f"Shiny's health is: {self.fleet.robot_fleet[2].health}")


        elif dinosaur == 'T-Rex':
            self.herd.dino_herd[1].attack(self.fleet.robot_fleet[0])
            if self.fleet.robot_fleet[0].health == 0 :
                self.herd.dino_herd[1].attack(self.fleet.robot_fleet[1])
                if self.fleet.robot_fleet[1].health == 0 :
                    self.herd.dino_herd[1].attack(self.fleet.robot_fleet[2])

        elif dinosaur == 'Terrordactyl':
            self.herd.dino_herd[2].attack(self.fleet.robot_fleet[0])
            if self.fleet.robot_fleet[0].health == 0 :
                self.herd.dino_herd[2].attack(self.fleet.robot_fleet[1])
                if self.fleet.robot_fleet[1].health == 0 :
                    self.herd.dino_herd[2].attack(self.fleet.robot_fleet[2])
        else:
            pass


    def robo_turn(self, robot):
        if robot == 'Scrappy':
            self.fleet.robot_fleet[0].attack(self.herd.dino_herd[0])
            if self.herd.dino_herd[0].health == 0 :
                self.fleet.robot_fleet[0].attack(self.herd.dino_herd[1])
                if self.herd.dino_herd[1].health == 0 :
                    self.fleet.robot_fleet[0].attack(self.herd.dino_herd[2])

        elif robot == 'Spare parts':
            self.fleet.robot_fleet[1].attack(self.herd.dino_herd[0])
            if self.herd.dino_herd[0].health == 0 :
                self.fleet.robot_fleet[1].attack(self.herd.dino_herd[1])
                if self.herd.dino_herd[1].health == 0 :
                    self.fleet.robot_fleet[1].attack(self.herd.dino_herd[2])

        elif robot == 'Shiny':
            self.fleet.robot_fleet[2].attack(self.herd.dino_herd[0])
            if self.herd.dino_herd[0].health == 0 :
                self.fleet.robot_fleet[2].attack(self.herd.dino_herd[1])
                if self.herd.dino_herd[1].health == 0 :
                    self.fleet.robot_fleet[2].attack(self.herd.dino_herd[2])


    def show_dino_opponent_options(self):
        pass


    def show_robo_opponent_options(self):
        pass


    def display_winners(self):
        if self.fleet == 0:
            print('The robots have won!')
            
        elif self.herd == 0:
            print('The dinos have won!')

            
