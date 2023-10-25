import random

class MazeGame:
    def __init__(self):
        self.maze = [[0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0]]

        self.player_position = (0, 0)

    def play(self):
        while True:
            # Display the maze to the player
            self.print_maze()

            # Get the player's move
            player_move = input("Enter a move (w, a, s, or d): ")

            # Move the player
            new_player_position = self.move_player(player_move)

            # Check if the player has reached the exit
            if self.maze[new_player_position[0]][new_player_position[1]] == 2:
                print("You win!")
                break

            # Check if the player has hit a wall
            if not self.is_valid_position(new_player_position):
                print("Invalid move.")
                continue

            # Update the player's position
            self.player_position = new_player_position

    def print_maze(self):
        for row in self.maze:
            for cell in row:
                if cell == 0:
                    print(" ", end="")
                elif cell == 1:
                    print("#", end="")
                elif cell == 2:
                    print("E", end="")
            print()

    def move_player(self, move):
        new_player_position = (self.player_position[0], self.player_position[1])

        if move == "w":
            new_player_position = (new_player_position[0] - 1, new_player_position[1])
        elif move == "a":
            new_player_position = (new_player_position[0], new_player_position[1] - 1)
        elif move == "s":
            new_player_position = (new_player_position[0] + 1, new_player_position[1])
        elif move == "d":
            new_player_position = (new_player_position[0], new_player_position[1] + 1)

        return new_player_position

    def is_valid_position(self, position):
        return 0 <= position[0] <= len(self.maze) - 1 and 0 <= position[1] <= len(self.maze[0]) - 1 and self.maze[position[0]][position[1]] != 1

# Create a new game
game = MazeGame()

# Play the game
game.play()
