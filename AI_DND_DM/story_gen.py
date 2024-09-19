import random
from typing import List, Dict

class QuestTemplate:
    def __init__(self, name: str, description: str, objectives: List[str], difficulty: int):
        self.name = name
        self.description = description 
        self.objectives = objectives 
        self.difficulty = difficulty 

class EnhancedStoryGenerator:
    def __init__(self):
        self.quest_template = [
            QuestTemplate(
                "The Lost Artifact",
                "An ancient artifact of immense power has been stolen from the city hall",
                ["Investigate city hall", "Track the thieves down", "Retrieve artifact"],
                3
            )
        ]

