class IGameEntity:
    def cast_fire(self): pass
    def swing(self): pass
    def unlock(self): pass
    def log(self, msg): pass

class Door(IGameEntity):
    def unlock(self):
        return "The door swings open."

class CursedStatue(Door):
    def unlock(self):
        raise Exception("I am a statue! I don't have a keyhole!")

class MegaHero(IGameEntity):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.weapon = "Excalibur" 
        
    def log(self, message):
        print(f"[LOG]: {self.name} {message}")

    def open_gate(self, key_type):
        if key_type == "Golden":
            self.log("Gate shines and slides open!")
        elif key_type == "Skeleton":
            self.log("Gate clicks and slowly opens.")
        else:
            self.log("Gate remains shut.")

    def attack_dragon(self):
        self.log(f"hits the Dragon with a divine slice of light from {self.weapon}!")


arthur = MegaHero("Arthur")
arthur.log("approaches the gate...")

arthur.open_gate("Golden") 
arthur.attack_dragon()


fake_door = CursedStatue()