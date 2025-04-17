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

class Matchup:
    """Represents a single game between two teams."""
    def __init__(self, team1, team2):
        names = ["Bob Evans", "Larry Jones", "Charlie West", "Jeff O'neill", "Clint Williams", "Earl Lake", "Tim Jon", "Bob Marley", "Snoop Dog", "Slim Shady", "John Doe", "John Cash", "Simon Claw", "Ted Bundy", "Michael Jordan", "Timmy Joe"]
        ref_name = random.choice(names)
        commentator_name = random.choice(names)
        self.team1 = team1
        self.team2 = team2
        self.winner = None
        self.team1_score = 0
        self.team2_score = 0
        self.arena = Arena(f"Arena {random.randint(1, 10)}", random.choice(["NY", "LA", "TX", "FL", "IL"]))
        self.referee = Referee(f"Ref", ref_name) 
        self.commentator = Commentator(f"Commentator", commentator_name) 
        self.fans = [Fan(f"Fan {i+1}", team1 if i % 2 == 0 else team2) for i in range(4)]
        self.team1_players = team1.players[:5]
        self.team1_bench = team1.players[5:]
        self.team2_players = team2.players[:5]
        self.team2_bench = team2.players[5:]

    def play_game(self):
        print(f" Tonight's game is between {self.team1} and {self.team2} and the tip off starts now!!")
        print(f"️ Game at {self.arena}")
        self.referee.officiate_game(self)
        self.commentator.provide_commentary(self)
        for fan in self.fans:
            fan.cheer()
        self.team1_score = sum(p.score_points() for p in self.team1_players + self.team1_bench)
        self.team2_score = sum(p.score_points() for p in self.team2_players + self.team2_bench)

        self.team1.total_points += self.team1_score
        self.team2.total_points += self.team2_score

        if self.team2_score <= self.team1_score:
            self.winner = self.team1
        else:
            self.winner = self.team2
            
        return self.winner, self.team1_players + self.team1_bench + self.team2_players + self.team2_bench

class AbstractRound(ABC):
    @abstractmethod
    def play_round(self):
        pass

class Round(AbstractRound):
    def __init__(self, teams, round_name):
        self.teams = teams
        self.round_name = round_name
        self.matchups = [Matchup(teams[i], teams[i + 1]) for i in range(0, len(teams), 2)]
        self.winners = []
        self.all_players = []

    def play_round(self):
        print(f"\n{self.round_name}:")
        for matchup in self.matchups:
            winner, players = matchup.play_game()
            print(f"{matchup.team1} vs {matchup.team2} -> Winner: {winner}")
            print(f"Score: {matchup.team1_score} - {matchup.team2_score}")
            print(f"{matchup.team1} Starting 5:")
            for player in matchup.team1_players:
                print(f"  {player}")
            print(f"{matchup.team1} Bench:")
            for player in matchup.team1_bench:
                print(f"  {player}")
            print(f"{matchup.team2} Starting 5:")
            for player in matchup.team2_players:
                print(f"  {player}")
            print(f"{matchup.team2} Bench:")
            for player in matchup.team2_bench:
                print(f"  {player}")
            self.winners.append(winner)
            self.all_players.extend(players)
        return self.winners, self.all_players
