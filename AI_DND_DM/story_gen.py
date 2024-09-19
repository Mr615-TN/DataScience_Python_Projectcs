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
            ),
            QuestTemplate(
                "Trouble in Mines",
                "The local mining operation has ceased and there have been strange noises reported from within",
                ["Explore the mines", "Discover the source of disturbance", "Resolve the situation"],
                2
            ),
        ] 
        self.locations = ["Forest", "Mountain","Desert", "Swamp", "City", "Village", "Dungeon", "Castle"]
        self.antagonists = ["Cult", "Dragon", "Demon", "Corrupt Noble", "Orc Warlod"]
    def generateQuest(self, party_level:int) -> Dict:
        template = random.choice(self.quest_template)
        location = random.choice(self.locations)
        antagonist = random.choice(self.antagonists)

        quest = {
            "name": template.name,
            "description": template.description,
            "location": location,
            "antagonist": antagonist,
            "objectives": template.objectives,
            "difficulty": min(template.difficulty + party_level -1,5),
            "rewards": self.generateRewards(template.difficulty, party_level)
        }

        quest["description"] = quest["description"].replace("the city", location.lower())
        quest["description"] += f"It's rumored that a {antagonist.lower()} is involved."
        
        return quest


