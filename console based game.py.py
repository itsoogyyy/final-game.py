import os
import time

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.winner = None
        self.game_running = True

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_board(self):
        self.clear_screen()
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")

    def print_board_with_positions(self):
        print("\nPosition numbers:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("\n")

    def make_move(self, position):
        position = int(position) - 1
        if 0 <= position <= 8 and self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                self.winner = self.board[i]
                return True

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                self.winner = self.board[i]
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            self.winner = self.board[0]
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            self.winner = self.board[2]
            return True

        return False

    def check_tie(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        print("Welcome to Tic Tac Toe!")
        print("Player 1 is X and Player 2 is O")
        time.sleep(2)

        while self.game_running:
            self.print_board()
            self.print_board_with_positions()
            
            print(f"Player {self.current_player}'s turn")
            position = input("Enter position (1-9): ")

            try:
                if not position.isdigit() or not 1 <= int(position) <= 9:
                    print("Please enter a number between 1 and 9")
                    time.sleep(1.5)
                    continue

                if not self.make_move(position):
                    print("Position already taken! Try again.")
                    time.sleep(1.5)
                    continue

                if self.check_winner():
                    self.print_board()
                    print(f"\nPlayer {self.winner} wins! 🎉")
                    self.game_running = False
                elif self.check_tie():
                    self.print_board()
                    print("\nIt's a tie! 🤝")
                    self.game_running = False
                else:
                    self.switch_player()

            except ValueError:
                print("Please enter a valid number!")
                time.sleep(1.5)

        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again.lower() == 'y':
            new_game = TicTacToe()
            new_game.play()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()