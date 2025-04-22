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

class TournamentBracket:
    def __init__(self, teams):
        self.teams = teams

class Tournament:
    def __init__(self, teams):
        self.bracket = TournamentBracket(sorted(teams, key=lambda t: t.seed))
        self.players_stats = []

    def run_tournament(self):
        rounds = [
            ("Round of 64", 64),
            ("Round of 32", 32),
            ("Sweet 16", 16),
            ("Elite 8", 8),
            ("Final 4", 4),
            ("Championship", 2)
        ]

        teams = self.bracket.teams
        for round_name, _ in rounds:
            round_obj = Round(teams, round_name)
            teams, players = round_obj.play_round()
            self.players_stats.extend(players)

        print(f"\n🏆 {teams[0]} WINS THE TOURNAMENT! 🏆")

        self.display_top_players()
        self.display_awards()
        self.display_team_stats(teams[0])

    def display_top_players(self):
        print("\n Top 5 Scorers of the Tournament:")
        
        # Deduplicate players by name
        player_map = {}
        for p in self.players_stats:
            player_map[p.name] = p  # Latest object kept

        unique_players = list(player_map.values())
        
        sorted_players = sorted(unique_players, key=lambda p: p.total_points, reverse=True)
        top_5 = sorted_players[:5]

        total_points = sum(p.total_points for p in top_5)
        total_assists = sum(p.total_assists for p in top_5)
        total_rebounds = sum(p.total_rebounds for p in top_5)
        total_steals = sum(p.total_steals for p in top_5)
        total_blocks = sum(p.total_blocks for p in top_5)
        total_fouls = sum(p.total_fouls for p in top_5)

        for i, player in enumerate(top_5, start=1):
            print(f"{i}. {player.position} - {player.name} ({player.team_name}) - {player.total_points} pts, {player.total_assists} ast, {player.total_rebounds} reb, {player.total_steals} stl, {player.total_blocks} blk, {player.total_fouls} fts")

        print("\n Combined Stats of Top 5 Players:")
        print(f"Total Points: {total_points}")
        print(f"Total Assists: {total_assists}")
        print(f"Total Rebounds: {total_rebounds}")
        print(f"Total Steals: {total_steals}")
        print(f"Total Blocks: {total_blocks}")
        print(f"Total Fouls: {total_fouls}")
        
    def display_awards(self):
        print("\n Tournament Awards:")
        
        player_map = {}
        for p in self.players_stats:
            player_map[p.name] = p

        players = list(player_map.values())
        mvp = max(players, key=lambda p: p.total_points)
        assist_leader = max(players, key=lambda p: p.total_assists)
        rebound_leader = max(players, key=lambda p: p.total_rebounds)
        defensive_leader = max(players, key=lambda p: p.total_steals + p.total_blocks)
        bench_players = [p for p in players if not p.is_starter]
        sixth_man = max(bench_players, key=lambda p: p.total_points)
        most_improved = max(players, key=lambda p: p.total_points / max(1, p.total_fouls))  # crude efficiency metric

        print(f"MVP: {mvp.name} {mvp.position} ({mvp.team_name}) - {mvp.total_points} points")
        print(f"Most Assists: {assist_leader.name} {assist_leader.position} ({assist_leader.team_name}) - {assist_leader.total_assists} assists")
        print(f"Most Rebounds: {rebound_leader.name} {rebound_leader.position} ({rebound_leader.team_name}) - {rebound_leader.total_rebounds} rebounds")
        print(f"Defensive Player of the Year: {defensive_leader.name} {defensive_leader.position} ({defensive_leader.team_name}) - {defensive_leader.total_steals} steals, {defensive_leader.total_blocks} blocks")
        print(f"Sixth Man of the Year: {sixth_man.name} {sixth_man.position} ({sixth_man.team_name}) - {sixth_man.total_points} points")
        print(f"Most Improved Player: {most_improved.name} {most_improved.position} ({most_improved.team_name}) - Efficiency: {most_improved.total_points} pts / {most_improved.total_fouls} fouls")
        
def display_team_stats(self, champion):
        print(f"\n {champion.name} Total Points Scored: {champion.total_points}")

class Scoreboard:
    def __init__(self):
        self.scores = {}

    def update_score(self, matchup, score):
        self.scores[matchup] = score

    def display_scores(self):
        for matchup, score in self.scores.items():
            print(f"{matchup}: {score}")

class Referee:
    def __init__(self,title, name):
        self.name = name

    def officiate_game(self, matchup):
        print(f"Referee {self.name} is officiating {matchup.team1} vs {matchup.team2}")

class Arena:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name} in {self.location}"

class Commentator:
    def __init__(self, title, name):
        self.name = name

    def provide_commentary(self, matchup):
        print(f"Commentator {self.name}: 'What a game between {matchup.team1} and {matchup.team2}!'")

class Fan:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def cheer(self):
        print(f"{self.name}: 'Go {self.team.name}!'")

class TournamentDirector:
    def __init__(self, name):
        self.name = name

    def start_tournament(self):
        print(f"Tournament Director {self.name} announces: 'Let the games begin!'")
    
def generate_teams():
    team_names = [
        "Crimson Raptors", "Blazing Tornadoes", "Golden Vipers", "Shadow Wolves", "Icy Hawks",
        "Electric Rhinos", "Lava Sharks", "Phantom Foxes", "Storm Kings", "Fire Falcons",
        "Iron Titans", "Venom Vultures", "Aqua Panthers", "Thundering Eagles", "Frost Giants",
        "Solar Bears", "Rogue Lions", "Steel Cobras", "Quantum Owls", "Mega Bulls",
        "Blitz Rams", "Chaos Cougars", "Nebula Tigers", "Galactic Gorillas", "Warp Jaguars",
        "Nova Pythons", "Plasma Gators", "Cyber Scorpions", "Crater Knights", "Dust Devils",
        "Warp Wolves", "Turbo Turtles", "Inferno Monkeys", "Doom Dragons", "Sky Krakens",
        "Tornado Tornadoes", "Pixel Phoenix", "Griffin Blades", "Blade Bison", "Rocket Rhinos",
        "Cobalt Bears", "Dark Dolphins", "Galaxy Ghosts", "Night Ninjas", "Dawn Demons",
        "Savage Swans", "Stealth Stingrays", "Howling Hounds", "Electric Emus", "Raging Raccoons",
        "Solar Sloths", "Nuclear Narwhals", "Meteor Minotaurs", "Hyper Hawks", "Zombie Zebras",
        "Omega Otters", "Chaos Chickens", "Flash Frogs", "Cyber Crows", "Polar Peacocks",
        "Warping Weasels", "Dark Dodos", "Velocity Vultures", "Robo Roosters"
    ]
    random.shuffle(team_names)
    teams = [Team(name, i + 1) for i, name in enumerate(team_names)]
    for team in teams:
        starting_five = [Player(generate_player_name(), team.name, position[i], is_starter = True) for i in range(5)]
        bench = [Player(generate_player_name(), team.name, random.choice(position), is_starter = False) for _ in range(3)]
        team.players = starting_five + bench
    return teams
def generate_player_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

if __name__ == "__main__":
    teams = generate_teams()
    director = TournamentDirector("John Smith") 
    try:
        with open("tournament_results.txt", "w", encoding="utf-8") as f:
            original_stdout = sys.stdout
            sys.stdout = f  # Redirect print output to the file

            director.start_tournament()
            tournament = Tournament(teams)
            tournament.run_tournament()
            f.flush() # Makes sure everything is written
        sys.stdout = original_stdout 
        print(" Tournament results exported to 'tournament_results.txt'")
    except Exception as e:
        # Restore stdout and print the error if something went wrong
        sys.stdout = original_stdout
        print(" Error during tournament:", e)
