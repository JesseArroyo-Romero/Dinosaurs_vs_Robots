from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dino_herd = []
    

    def create_herd(self):
        dino_one = Dinosaur('Velociraptor', 100, 2000)
        dino_two = Dinosaur('T-Rex', 200, 2500)
        dino_three = Dinosaur('Terrordactyl', 150, 1800)
        self.dino_herd.append(dino_one, dino_two, dino_three)
       
    
       