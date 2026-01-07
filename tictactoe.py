import os
import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current = 'X'
        self.game_over = False
        self.winner = None

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n  1 | 2 | 3")
        print(" ---|---|---")
        print("  4 | 5 | 6")
        print(" ---|---|---")
        print("  7 | 8 | 9\n")
        print(" Текущая доска:")
        for i in range(3):
            row = self.board[i*3:(i+1)*3]
            print(f"  {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print(" ---|---|---")
        print()

    def move(self, pos):
        if self.board[pos] == ' ':
            self.board[pos] = self.current
            if self.check_win():
                self.winner = self.current
                self.game_over = True
            elif ' ' not in self.board:
                self.game_over = True
            else:
                self.current = 'O' if self.current == 'X' else 'X'
            return True
        return False

    def check_win(self):
        wins = [[0,1,2],[3,4,5],[6,7,8],
                [0,3,6],[1,4,7],[2,5,8],
                [0,4,8],[2,4,6]]
        for a,b,c in wins:
            if self.board[a]==self.board[b]==self.board[c]!=' ':
                return True
        return False

    def available(self):
        return [i for i,x in enumerate(self.board) if x==' ']

def play():
    game = TicTacToe()
    mode = input("1 - с игроком\n2 - с компьютером\nВыбор: ")
    
    while not game.game_over:
        game.display()
        
        if game.current == 'X' or mode == '1':
            try:
                pos = int(input(f"Ход {game.current} (1-9): ")) - 1
                if not 0 <= pos <= 8:
                    continue
                if not game.move(pos):
                    print("Клетка занята!")
                    input("Enter...")
            except:
                continue
        else:
            moves = game.available()
            if moves:
                pos = random.choice(moves)
                game.move(pos)
                input("Компьютер сходил...")
    
    game.display()
    if game.winner:
        print(f"Победил {game.winner}!")
    else:
        print("Ничья!")
    input("Enter...")

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Крестики-нолики")
        print("1 - Играть")
        print("2 - Выйти")
        if input("Выбор: ") == '1':
            play()
        else:
            break