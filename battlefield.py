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
        


    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs!')


    def battle(self):
        fight = True
        while fight == True:
            self.dino_turn('Velociraptor')
            self.dino_turn('T-Rex')
            self.dino_turn('Terrordactyl')
            self.robo_turn('Scrappy')
            self.robo_turn('Spare parts')
            self.robo_turn('Shiny')
            if self.fleet.robot_fleet == 0:
                fight == False
                self.display_winners()

            elif self.herd.dino_herd == 0:
                fight == False
                self.display_winners()         
      
    
    def dino_turn(self, dinosaur):
        if self.fleet.robot_fleet != 0:
                if dinosaur == f"{self.herd.dino_herd[0]}":
                    if self.herd.dino_herd[0].health <= 0:
                        del self.herd.dino_herd[0]
                    else:
                        print(f'Look at {self.herd.dino_herd[0]} go!')
                        self.herd.dino_herd[0].attack(self.fleet.robot_fleet[0])
                        print(f"{self.fleet.robot_fleet[0]}'s health is: {self.fleet.robot_fleet[0].health}")
                              

                elif dinosaur == f"{self.herd.dino_herd[1]}" or f"{self.herd.dino_herd[1]}" == f"{self.herd.dino_herd[0]}":
                    if self.herd.dino_herd[1].health <= 0 :
                        del self.herd.dino_herd[1]
                    else:
                        print(f"Look at {self.herd.dino_herd[1]} go! ")
                        self.herd.dino_herd[1].attack(self.fleet.robot_fleet[0])
                        print(f"{self.fleet.robot_fleet[0]}'s health is: {self.fleet.robot_fleet[0].health}")

                elif dinosaur == "Terrordactyl":
                    if self.herd.dino_herd[2].health <= 0 or self.herd.dino_herd[2] == self.herd.dino_herd[1]:
                        del self.herd.dino_herd[2]
                        del self.herd.dino_herd[1]
                    else:
                        print(f"Alright {self.herd.dino_herd[2]}, your turn!")
                        self.herd.dino_herd[2].attack(self.fleet.robot_fleet[0])
                        print(f"Scrappy's health is: {self.fleet.robot_fleet[0].health}")          

        elif self.fleet.robot_fleet == 0:
            self.display_winners


    def robo_turn(self, robot):
        if self.herd.dino_herd != 0:
            if robot == f"{self.fleet.robot_fleet[0]}":
                if self.fleet.robot_fleet[0].health <= 0 :
                    del self.fleet.robot_fleet[0]
                    print(self.fleet.robot_fleet)
                else:
                    print(f"Alright {self.fleet.robot_fleet[0]}, your turn!")
                    self.fleet.robot_fleet[0].attack(self.herd.dino_herd[0])
                    print(f"{self.herd.dino_herd[0]}'s remaining health is: {self.herd.dino_herd[0].health}")

            elif robot == 'Spare parts':
                if robot == 'Spare parts':
                    if self.fleet.robot_fleet[0].health <= 0:
                        del self.fleet.robot_fleet[0]
                        print(self.fleet.robot_fleet)
                    print(f"Let's go {self.fleet.robot_fleet[0]}")
                    self.fleet.robot_fleet[0].attack(self.herd.dino_herd[0])
                    print(f"{self.herd.dino_herd[0]}'s health is: {self.herd.dino_herd[0].health}")
                
                else:
                    print(f"Let's go {robot}!")
                    self.fleet.robot_fleet[1].attack(self.herd.dino_herd[0])
                    print(f"{self.herd.dino_herd[0]}'s health is: {self.herd.dino_herd[0].health}")

            elif robot == 'Shiny' :
                print(self.fleet.robot_fleet)
                if robot == "Shiny":
                    if self.fleet.robot_fleet[1].health <= 0:
                        del self.fleet.robot_fleet[1]
                        print(self.fleet.robot_fleet)
                        self.robo_turn(self)
                    print(f"Let's go {self.fleet.robot_fleet[1]}!")
                    self.fleet.robot_fleet[1].attack(self.herd.dino_herd[0])
                    print(f"{self.herd.dino_herd[0]}'s health is: {self.herd.dino_herd[0].health}")
                
                else:
                    print(f"Let's go {robot}!")
                    self.fleet.robot_fleet[2].attack(self.herd.dino_herd[0])
                    print(f"{self.herd.dino_herd[0]}'s health is: {self.herd.dino_herd[0].health}")
                
        elif self.herd.dino_herd == 0:
            self.display_winners()
            
        

    def show_dino_opponent_options(self):
        pass


    def show_robo_opponent_options(self):
        pass


    def display_winners(self):
        if self.fleet.robot_fleet == 0:
            print('The robots have won!')
            
        elif self.herd.dino_herd == 0:
            print('The dinos have won!')

            
