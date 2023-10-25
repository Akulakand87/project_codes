#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_TRIES 6
#define MAX_WORD_LENGTH 20

int main() {
    char word[MAX_WORD_LENGTH];
    char guessed[MAX_WORD_LENGTH];
    int tries = 0;
    int wordLength, i;
    char guess;

    printf("Welcome to Hangman!\n");
    printf("Enter the word to be guessed: ");
    scanf("%s", word);

    wordLength = strlen(word);

    for (i = 0; i < wordLength; i++) {
        guessed[i] = '_';
    }
    guessed[wordLength] = '\0';

    while (tries < MAX_TRIES && strcmp(word, guessed) != 0) {
        printf("\nWord: %s\n", guessed);
        printf("Tries left: %d\n", MAX_TRIES - tries);
        printf("Enter your guess: ");
        scanf(" %c", &guess);
        guess = tolower(guess);

        int found = 0;
        for (i = 0; i < wordLength; i++) {
            if (word[i] == guess) {
                guessed[i] = guess;
                found = 1;
            }
        }

        if (!found) {
            tries++;
            printf("Incorrect guess!\n");
        }
    }

    if (strcmp(word, guessed) == 0) {
        printf("\nCongratulations! You guessed the word: %s\n", word);
    } else {
        printf("\nSorry, you ran out of tries. The word was: %s\n", word);
    }

    return 0;
}
