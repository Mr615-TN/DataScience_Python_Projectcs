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
    def __init__(self) -> None:
        pass