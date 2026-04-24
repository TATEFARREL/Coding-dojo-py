from abc import ABC, abstractmethod

# 1. SRP: The Hero handles health; the Journal handles logging.
class Journal:
    def log(self, message):
        print(f"[LOG]: {message}")

class Hero:
    def __init__(self, name, journal):
        self.name, self.hp, self.journal = name, 100, journal
    def act(self, msg): self.journal.log(f"{self.name} {msg}")

# 2. OCP: The Gate works with any 'Key' without being modified.
class Key(ABC):
    @abstractmethod
    def unlock(self): pass

class GoldenKey(Key):
    def unlock(self): return "shines and slides open!"

class Gate:
    def open_with(self, key): print(f"The gate {key.unlock()}")

# 3. LSP: Use 'Interactable' instead of forcing a Statue to be a Platform.
class Interactable(ABC):
    @abstractmethod
    def interact(self): pass

class CursedStatue(Interactable):
    def interact(self): return "The statue whispers... but stays put."

# 4. ISP: Split the giant 'Spell' interface into specific skills.
class FireCaster(ABC):
    @abstractmethod
    def cast_fire(self): pass

class FireScroll(FireCaster):
    def cast_fire(self): print("Fireball launched!")

# 5. DIP: Dragon depends on 'Weapon' (abstraction), not a specific sword.
class Weapon(ABC):
    @abstractmethod
    def swing(self): pass

class Excalibur(Weapon):
    def swing(self): return "a divine slice of light!"

class Dragon:
    def __init__(self, weapon): # Injected via constructor
        self.weapon = weapon
    def take_hit(self): print(f"Dragon hit by {self.weapon.swing()}")

# --- RUNNING THE ADVENTURE ---
log = Journal()
hero = Hero("Arthur", log)
hero.act("approaches the gate...")

Gate().open_with(GoldenKey())
Dragon(Excalibur()).take_hit()
