import random

class MemoryGame:
    def __init__(self):
        self.cards = []
        for i in range(16):
            self.cards.append(i // 2)

        random.shuffle(self.cards)

        self.flipped_cards = []

    def play(self):
        while True:
            # Display the cards to the player
            self.print_cards()

            # Get the player's move
            player_move = input("Enter two cards to flip (row, column): ")

            # Validate the move
            if not isinstance(player_move, (tuple, list)) or len(player_move) != 2:
                print("Invalid move.")
                continue

            row1, column1 = player_move[0]
            row2, column2 = player_move[1]

            if not isinstance(row1, int) or not isinstance(column1, int) or not isinstance(row2, int) or not isinstance(column2, int):
                print("Invalid move.")
                continue

            if row1 < 0 or row1 >= 4 or column1 < 0 or column1 >= 4 or row2 < 0 or row2 >= 4 or column2 < 0 or column2 >= 4:
                print("Invalid move.")
                continue

            if (row1, column1) in self.flipped_cards or (row2, column2) in self.flipped_cards:
                print("Invalid move.")
                continue

            # Flip the cards
            self.flipped_cards.append((row1, column1))
            self.flipped_cards.append((row2, column2))

            # Check if the cards are a match
            if self.cards[row1][column1] == self.cards[row2][column2]:
                # Remove the cards from the board
                self.cards.remove(self.cards[row1][column1])
                self.cards.remove(self.cards[row2][column2])

                # Check if the game is over
                if not self.cards:
                    print("You win!")
                    break
            else:
                # Flip the cards back over
                self.flipped_cards.remove((row1, column1))
                self.flipped_cards.remove((row2, column2))

    def print_cards(self):
        for row in range(4):
            print("+---+---+---+---+")
            for column in range(4):
                if (row, column) in self.flipped_cards:
                    print("| {} ", self.cards[row][column], end="")
                else:
                    print("|   ", end="")
            print("|")
        print("+---+---+---+---+")

# Create a new game
game = MemoryGame()

# Play the game
game.play()
