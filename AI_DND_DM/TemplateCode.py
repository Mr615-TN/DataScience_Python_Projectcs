import random
from typing import List, Dict

class Character:
    def __init__(self, name: str, character_class: str, level: int):
        self.name = name
        self.character_class = character_class
        self.level = level
        self.hp = 0
        self.stats = {}
        self.inventory = {}

class NPC:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.hp = 0
        self.stats = {}

class Location:
    def __init__(self, name = str, description = str):
        self.name = name
        self.description = description
        self.npcs = []
        self.items = []

class StoryGenerator:
    def generate_quest(self) -> str:
        quests = [
            "Retrieve a magical artifact from an ancient kingdom",
            "Rescue a kidnapped noble from a band of orcs",
            "Clear out a cave that has been infested by a horde of orcs and goblins",
            "Broker peace between two warring factions",
            "Investigate an ancient ruin near a village of humans that has been taken over by dark elves"
        ]
        return random.choice(quests)
    
class CombatSystem:
    def __init__(self):
        self.initiativeOrder = []
    
    def roll_order(self, characters: List[Character]):
        self.initiativeOrder = [(char, random.randint(1,20)) for char in characters]
        self.initiativeOrder.sort(key=lambda x: x[1], reverse=True)
    
    def process_combat_round(self):
        for character, _ in self.initiativeOrder:
            print(f"{character.name}'s turn ...")
    

class DungeonMaster:
    def __init__(self):
        self.storygen = StoryGenerator()
        self.combat_sys = CombatSystem()
        self.current_loc = None
        self.characters = []

    def startGame(self):
        print("Welcome to the AI D&D Game!")
        self.create_characters()
        self.generate_start_loc()
        self.main_gameLoop()
    
    def create_characters(self):
        num_players = int(input("How many people are playing?"))
        for i in range(num_players):
            name = input(f"Enter name for character {i+1}: ")
            class_character = input(f"Enter class for {name}: ")
            self.characters.append(Character(name, class_character, 1))
    
    def generate_start_loc(self):
        self.current_loc = Location("Village of Hillystone", "A small and peaceful village that is nestled in a valley")

    def main_gameLoop(self):
        while True:
            self.describe_currentLoc()
            action = input("What would you like to do? ").lower()
            if action == "quit":
                break
            elif action == "look around":
                self.talk_npc()
            elif action == "fight"
                self.initiateFight()
            else:
                print("I dont understand the action")

    def describe_currentLoc(self):
        print(f"\nYou are in {self.current_loc.name}.")
        print(self.current_loc.description)

    def talk_npc(self):
        if not self.current_loc.npcs:
            print("There is currently no one here to talk to")
            return
        npc = random.choice(self.current_loc.npcs)
        print(f"You approach {npc.name}.{npc.description}")

    def initiateFight(self):
        enemies = [Character(f"Goblin {i}", "Goblin", 1) for i in range(3)]
        allCombatants = self.characters + enemies
        self.combat_sys.roll_order(allCombatants)
        print("Combat has been initiated! Rolling for initiative!")
        for character, initiative in self.combat_sys.initiativeOrder:
            print(f"{character.name}: {initiative}")
        self.combat_sys.process_combat_round()

__name__ == "__main__":
    dm = DungeonMaster()
    dm.startGame()


    
        
