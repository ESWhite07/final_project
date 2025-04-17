from abc import ABC, abstractmethod
import random
from collections import defaultdict
import sys
import json
import os

position = ["PG","SG", "SF", "PF", "C"]
        
first_names = [
    "Jordan", "Taylor", "Casey", "Alex", "Chris", "Riley", "Morgan", "Skyler",
    "Jesse", "Avery", "Blake", "Jamie", "Quinn", "Logan", "Dakota", "Cameron",
    "Hunter", "Devon", "Parker", "Rowan", "Spencer", "Elliot", "Micah", "Reese",
    "Shawn", "Drew", "Morgan", "Terry", "Kendall", "Reagan", "Zion", "Jayden",
    "Marley", "Kai", "Phoenix", "Emerson", "Remy", "Oakley", "Angel", "Tatum",
    "Case", "Sky", "Ryan", "Harley", "Sage", "Eden", "Luca", "August", "Toby",
    "Shiloh", "River", "Jaden", "Noel", "Justice", "Frankie", "Corey", "Ari",
    "Toni", "Dylan", "Rory", "Indigo"
]
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Murphy", "Reed", "Cook", "Rogers", "Morgan",
    "Cooper", "Cox", "Diaz", "Gray"
]
class Team:
    """Represents a basketball team."""
    def __init__(self, name, seed):
        self.name = name
        self.seed = seed
        self.total_points = 0
        self.player = []

    def __str__(self):
        return f"{self.name} (Seed {self.seed})"
class Player:
    """Represents a player in a team."""
    def __init__(self, name, team_name, position, is_starter = True):
        self.name = name
        self.points = 0
        self.total_points = 0
        self.assists = 0
        self.total_assists = 0
        self.rebounds = 0
        self.total_rebounds = 0
        self.steals = 0
        self.total_steals = 0
        self.blocks = 0
        self.total_blocks = 0
        self.fouls = 0
        self.total_fouls = 0
        self.team_name = team_name
        self.position = position
        self.is_starter = is_starter

    def score_points(self):
        self.points = random.randint(0, 30)
        self.assists = random.randint(0, 10)
        self.rebounds = random.randint(0, 10)
        self.steals = random.randint(0,5)
        self.blocks = random.randint(0,5)
        self.fouls = random.randint(0,5)
        self.total_points += self.points
        self.total_assists += self.assists
        self.total_rebounds += self.rebounds
        self.total_steals += self.steals
        self.total_blocks += self.blocks
        self.total_fouls += self.fouls
        if self.fouls >= 6:
            print(f"{self.name} has fouled out!")
            self.points = 0  
        return self.points

    def __str__(self):
        return (f"{self.position} - {self.name}: {self.points} pts, {self.assists} ast, {self.rebounds} reb "
                f"{self.steals} stl, {self.blocks} blk, {self.fouls} fts "
                f"(Total: {self.total_points} pts, {self.total_assists} ast, {self.total_rebounds} reb)"f"{self.total_steals} stl, {self.total_blocks} blk, {self.total_fouls} fts)")
    
def generate_player_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"
