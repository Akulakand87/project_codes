#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int playerChoice, computerChoice;
    
    // Seed the random number generator
    srand(time(0));
    
    printf("Welcome to Rock, Paper, Scissors!\n");
    printf("1. Rock\n");
    printf("2. Paper\n");
    printf("3. Scissors\n");
    printf("Enter your choice (1-3): ");
    scanf("%d", &playerChoice);
    
    // Generate a random choice for the computer
    computerChoice = rand() % 3 + 1;
    
    printf("\n");
    
    // Determine the winner
    if (playerChoice == computerChoice) {
        printf("It's a tie!\n");
    } else if ((playerChoice == 1 && computerChoice == 3) ||
               (playerChoice == 2 && computerChoice == 1) ||
               (playerChoice == 3 && computerChoice == 2)) {
        printf("You win!\n");
    } else {
        printf("Computer wins!\n");
    }
    
    return 0;
}
