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
            if len(self.fleet.robot_fleet) == 0:
                fight == False
                self.display_winners()
                return fight

            elif len(self.herd.dino_herd) == 0:
                fight == False
                self.display_winners()  
                return fight       
      
    
    def dino_turn(self, dinosaur):
        if len(self.fleet.robot_fleet) == 0:
                self.display_winners()
        elif len(self.fleet.robot_fleet) != 0:
                
                if len(self.herd.dino_herd) == 3:
                        if dinosaur == f"{self.herd.dino_herd[0]}":
                                print(f'Look at {self.herd.dino_herd[0]} go!')
                                self.herd.dino_herd[0].attack(self.fleet.robot_fleet[0])
                                print(f"{self.fleet.robot_fleet[0]}'s health is: {self.fleet.robot_fleet[0].health}")
                                if self.fleet.robot_fleet[0].health <= 0:
                                        del self.fleet.robot_fleet[0]
                                
                        elif dinosaur == f"{self.herd.dino_herd[1]}" :
                                print(f"Look at {self.herd.dino_herd[1]} go! ")
                                self.herd.dino_herd[1].attack(self.fleet.robot_fleet[0])
                                print(f"{self.fleet.robot_fleet[0]}'s health is: {self.fleet.robot_fleet[0].health}")
                                if self.fleet.robot_fleet[0].health <= 0:
                                        del self.fleet.robot_fleet[0]
                                
                        elif dinosaur == f"{self.herd.dino_herd[2]}" :
                                print(f"Alright {self.herd.dino_herd[2]}, your turn!")
                                self.herd.dino_herd[2].attack(self.fleet.robot_fleet[0])
                                print(f"{self.fleet.robot_fleet[0]}'s health is: {self.fleet.robot_fleet[0].health}")
                                if self.fleet.robot_fleet[0].health <= 0:
                                        del self.fleet.robot_fleet[0]
                                
                if len(self.herd.dino_herd) == 2:
                        if dinosaur == f"{self.herd.dino_herd[0]}":
                                print(f'Look at {self.herd.dino_herd[0]} go!')
                                self.herd.dino_herd[0].attack(self.fleet.robot_fleet[0])
                                print(f"{self.fleet.robot_fleet[0]}'s health is: {self.fleet.robot_fleet[0].health}")
                                if self.fleet.robot_fleet[0].health <= 0:
                                        del self.fleet.robot_fleet[0]
                                                                
                        elif dinosaur == f"{self.herd.dino_herd[1]}" :
                                print(f"Look at {self.herd.dino_herd[1]} go! ")
                                self.herd.dino_herd[1].attack(self.fleet.robot_fleet[0])
                                print(f"{self.fleet.robot_fleet[0]}'s health is: {self.fleet.robot_fleet[0].health}")
                                if self.fleet.robot_fleet[0].health <= 0:
                                        del self.fleet.robot_fleet[0]

                if len(self.herd.dino_herd) == 1:
                        if dinosaur == f"{self.herd.dino_herd[0]}":
                                print(f'Look at {self.herd.dino_herd[0]} go!')
                                self.herd.dino_herd[0].attack(self.fleet.robot_fleet[0])
                                print(f"{self.fleet.robot_fleet[0]}'s health is: {self.fleet.robot_fleet[0].health}")
                                if self.fleet.robot_fleet[0].health <= 0:
                                        del self.fleet.robot_fleet[0]
                                
       
        
    def robo_turn(self, robot):
        if len(self.herd.dino_herd) == 0:
                    self.display_winners()
        elif len(self.herd.dino_herd) != 0:

                if len(self.fleet.robot_fleet) == 3 :
                        if robot == f"{self.fleet.robot_fleet[0]}" :
                                print(f"Alright {self.fleet.robot_fleet[0]}, your turn!")
                                self.fleet.robot_fleet[0].attack(self.herd.dino_herd[0])
                                print(f"{self.herd.dino_herd[0]}'s remaining health is: {self.herd.dino_herd[0].health}")
                                if self.herd.dino_herd[0].health <= 0:
                                        del self.herd.dino_herd[0]
                                
                        elif robot == f"{self.fleet.robot_fleet[1]}" :
                                print(f"Let's go {self.fleet.robot_fleet[1]}")
                                self.fleet.robot_fleet[1].attack(self.herd.dino_herd[0])
                                print(f"{self.herd.dino_herd[0]}'s health is: {self.herd.dino_herd[0].health}")
                                if self.herd.dino_herd[0].health <= 0:
                                        del self.herd.dino_herd[0]
                                
                        elif robot == f"{self.fleet.robot_fleet[2]}":
                                print(f"Let's go {self.fleet.robot_fleet[2]}!")
                                self.fleet.robot_fleet[2].attack(self.herd.dino_herd[0])
                                print(f"{self.herd.dino_herd[0]}'s health is: {self.herd.dino_herd[0].health}")
                                if self.herd.dino_herd[0].health <= 0:
                                        del self.herd.dino_herd[0]
                                
                if len(self.fleet.robot_fleet) == 2 :
                        if robot == f"{self.fleet.robot_fleet[0]}" :
                                print(f"Alright {self.fleet.robot_fleet[0]}, your turn!")
                                self.fleet.robot_fleet[0].attack(self.herd.dino_herd[0])
                                print(f"{self.herd.dino_herd[0]}'s remaining health is: {self.herd.dino_herd[0].health}")
                                if self.herd.dino_herd[0].health <= 0:
                                        del self.herd.dino_herd[0]
                                
                        elif robot == f"{self.fleet.robot_fleet[1]}" :
                                print(f"Let's go {self.fleet.robot_fleet[1]}")
                                self.fleet.robot_fleet[1].attack(self.herd.dino_herd[0])
                                print(f"{self.herd.dino_herd[0]}'s health is: {self.herd.dino_herd[0].health}")
                                if self.herd.dino_herd[0].health <= 0:
                                        del self.herd.dino_herd[0]
                                                
                if len(self.fleet.robot_fleet) == 1 :
                        if robot == f"{self.fleet.robot_fleet[0]}" :
                                print(f"Alright {self.fleet.robot_fleet[0]}, your turn!")
                                self.fleet.robot_fleet[0].attack(self.herd.dino_herd[0])
                                print(f"{self.herd.dino_herd[0]}'s remaining health is: {self.herd.dino_herd[0].health}")
                                if self.herd.dino_herd[0].health <= 0:
                                        del self.herd.dino_herd[0]
                                            
        elif self.herd.dino_herd == 0:
            self.display_winners()
            
        

    def show_dino_opponent_options(self):
        pass


    def show_robo_opponent_options(self):
        pass


    def display_winners(self):
        if len(self.fleet.robot_fleet) == 0:
            print('The dinos have won!')
            
        elif len(self.herd.dino_herd) == 0:
            print('The robots have won!')

            
