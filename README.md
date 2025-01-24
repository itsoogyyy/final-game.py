# FINAL GAME CONSOLE PETA
final performance task 

# Game Overview
-The game uses these variables to create a complete, interactive Tic Tac Toe experience where two players can take turns until someone wins or the game ends in a tie.


# Game mechanics
Game Initialization:
Game starts with an empty 3x3 board
Player "X" always goes first
Board positions are numbered 1-9 (for user input)

Turn System:
Players alternate between "X" and "O"
Each turn consists of
Displaying the current board
Showing position numbers (1-9)
Prompting current player for input
Validating and making the move
Checking for win/tie conditions
Switching to the other player

Move Validation:
Checks if input is a number between 1-9
Verifies if the chosen position is empty
Prevents playing in already occupied positions

Win Conditions:
(checked after each move)
Three in a row horizontally (positions [0,1,2], [3,4,5], or [6,7,8])
Three in a row vertically (positions [0,3,6], [1,4,7], or [2,5,8])
Three in a row diagonally (positions [0,4,8] or [2,4,6])

Tie Condition:
Occurs when all positions are filled
No player has achieved a winning combination
Game Flow Control
Game continues until there's a winner or tie
Clear screen after each move for better visibility
1.5 second delay after invalid moves
2 second delay at game start

Error Handling:
Handles invalid inputs (non-numbers)
Prevents out-of-range moves
Provides feedback for invalid moves
Play Again Feature
After game ends, offers to start a new game
Creates fresh game instance if player chooses to continue




# Variables used 
self.board: A list of 9 elements (initialized with spaces) representing the 3x3 game board
Each position can contain " " (empty), "X", or "O"
Positions are numbered 0-8, arranged in a 3x3 grid:
self.current_player: A string that keeps track of whose turn it is
Alternates between "X" and "O"
"X" starts the game by default

self.winner: Stores the winner of the game
Initially set to None
Will be set to "X" or "O" when someone wins
Can be set to "Tie" if the game ends in a draw
self.game_running: A boolean flag that controls the game loop
True while the game is in progress
Set to False when the game ends (either by win or draw)

position: Used in the make_move method
Input from the player (1-9)
Converted to 0-8 internally (by subtracting 1)
Represents where the player wants to place their mark
Winning combinations are checked in check_winner:[

Rows: positions [0,1,2], [3,4,5], [6,7,8]
Columns: positions [0,3,6], [1,4,7], [2,5,8]
Diagonals: positions [0,4,8], [2,4,6]
Game states:
Empty space: " " (a single space)
Player marks: "X" and "O"
Valid positions: 1-9 (user input) or 0-8 (internal board representation)
These variables work together to:

Track the game state (board)
Manage turns (current_player)
Handle game progression (game_running)
Determine the outcome (winner)
Process player moves (position)

