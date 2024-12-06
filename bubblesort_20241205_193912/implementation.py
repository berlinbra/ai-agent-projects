class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def display_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        if ' ' not in self.board:
            return 'Tie'
        return None

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.display_board()

        while True:
            position = int(input(f"Player {self.current_player}, enter a position (0-8): "))
            if self.make_move(position):
                self.display_board()
                winner = self.check_winner()
                if winner:
                    if winner == 'Tie':
                        print("It's a tie!")
                    else:
                        print(f"Player {winner} wins!")
                    break
            else:
                print("Invalid move. Try again.")

if __name__ == '__main__':
    game = TicTacToe()
    game.play()