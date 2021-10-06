from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dino_one = Dinosaur('Velociraptor', 100, 2000)
        self.dino_two = Dinosaur('T-Rex', 200, 2500)
        self.dino_three = Dinosaur('Terrordactyl', 150, 1800)
    

    def create_herd(self):
        self.dino_herd = [self.dino_one, self.dino_two, self.dino_three]
