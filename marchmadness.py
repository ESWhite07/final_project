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
