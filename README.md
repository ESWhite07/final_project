# March Madness Project
_March Madness Simulator_

A Python-based basketball tournament simulator where randomly generated players form teams and compete in a playoff-style tournament. The simulator tracks player statistics, determines award winners, and maintains a Hall of Fame record over multiple runs.


**Features**

Team and Player Generation: Each team consists of 5 starters and 2 bench players with random attributes.

Game Simulation: Matches simulate points, assists, rebounds, and fouls.

Elimination Bracket: Single-elimination tournament format until a champion is crowned.


**Player Awards:**

Most Valuable Player (MVP)

Tracks Most Assists in the Year

Defensive Player of the Year (most rebounds)

Sixth Man of the Year (top bench scorer)

Most Improved Player (highest improvement factor)

Fouling Out: Players foul out if they reach a foul limit.

Hall of Fame Tracking: Award winners and notable stats are saved to a persistent hall_of_fame.txt file after each tournament.

Fans, Referees, and Commentators: Randomly generated to add personality to games.


**Requirements**

Python 3.7+

No external libraries are needed beyond the Python Standard Library.


**How to Run**

Clone or download the repository.

Ensure hall_of_fame.txt is in the same directory (it will auto-create if missing).

Run the simulator:

python tournament_simulator.py


**Notes**

Hall of Fame: The simulator appends new award winners after each tournament under a "New Tournament" marker.

Sixth Man Award: Only awarded if there are eligible bench players who scored during games.

MVP Calculation: MVP is selected based on total points scored. (Optional upgrade: use a weighted formula with assists and rebounds.)

Randomness: Outcomes vary on each run due to random generation.


**Future Improvements**

Export detailed player stats to CSV.

Add user interaction: team selection or custom player creation.

More detailed commentary and fan impact on games.


**Author**

Developed by Elijah White.

**License**

This project is open source and free to use.

A puml diagram will also be put into this git repository so you can see an in depth structure of how the classes all work together.
