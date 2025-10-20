class Player:
    #تهيئة اسم ورمز اللاعب
    def init(self):
        self.name = ""
        self.symbol = ""
#طلب ادخال اسم اللاعب
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ").strip()
            if name.isalpha():
                self.name = name
                break
            print("Invalid name, please enter letters only.")
#طلب اختيار رمز اللاعب
    def choose_symbol(self, taken_symbols=None):
        if taken_symbols is None:
            taken_symbols = set()
        while True:
            symbol = input("Enter your symbol (a single letter): ").strip()
            if symbol.isalpha() and len(symbol) == 1:
                if symbol in taken_symbols:
                    print("Symbol already taken, choose another one.")
                    continue
                self.symbol = symbol
                break
            print("Invalid symbol, please enter a single letter.")


class Menu:
    #عرض خيارات القائمة الرئيسية
    def display_main_menu(self):
        print("\nWelcome to my X_O game")
        print("1. Start game")
        print("2. Quit game")
        choice = input("Enter your choice (1 or 2): ").strip()
        return choice
#عرض خيارات قائمة نهاية اللعبة
    def display_endgame_menu(self):
        print("\nGame Over!")
        print("1. Restart game")
        print("2. Quit game")
        choice = input("Enter your choice (1 or 2): ").strip()
        return choice


class Board:
    #تهيئة لوحة اللعبة بالارقام من 1 الى 9
    def init(self):
        self.board = [str(i) for i in range(1, 10)]
#عرض الحالة الحالية للوحة
    def display_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i + 3]))
            if i < 6:
                print("-" * 9)
#تحديث اللوحة بالرمز اذا الحركة صح
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False
#التحقق اذا الخانة متاحة
    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()
#اعادة تعيين اللوحة الى حالتها الاولية
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(), Player()]
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        #الحلقة الرئيسية للبدء
        while True:
            choice = self.menu.display_main_menu()
            if choice == "1":
                self.setup_players()
                self.play_game()
            elif choice == "2":
                self.quit_game()
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
#اعداد اللاعبين
    def setup_players(self):
        taken = set()
        for number, player in enumerate(self.players, start=1):
            print(f"\nPlayer {number}, enter your details:")
            player.choose_name()
            player.choose_symbol(taken_symbols=taken)
            taken.add(player.symbol)
            print("-" * 20)

    def play_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        while True:
            self.play_turn()
            if self.check_win():
                self.board.display_board()
                print(f"\n{self.players[self.current_player_index].name} wins! 🏆")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.board.reset_board()
                    self.current_player_index = 0
                    continue
                else:
                    self.quit_game()
                    break
            elif self.check_draw():
                self.board.display_board()
                print("\nIt's a draw! 😐")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.board.reset_board()
                    self.current_player_index = 0
                    continue
                else:
                    self.quit_game()
                    break
            self.switch_player()
    def play_turn(self):
             #ادخال اللاعب
             player = self.players[self.current_player_index]
             self.board.display_board()
             print(f"{player.name}'s turn ({player.symbol})")
             while True:
               try:
                 cell_choice = int(input("Choose a cell (1-9): ").strip())
                 if 1 <= cell_choice <= 9:
                    if self.board.update_board(cell_choice, player.symbol):
                      break
                    else:
                        print("Cell already taken, try again.")
                 else:
                    print("Please enter a number between 1 and 9.")
               except ValueError:
                print("Please enter a number between 1 and 9.")

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        cells = self.board.board
        winning = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning:
            a, b, c = combo
            if cells[a] == cells[b] == cells[c] and not cells[a].isdigit():
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def quit_game(self):
        print("\nThank you for playing! 👋")


if __name__ == "__main__":
    game = Game()
    game.start_game()