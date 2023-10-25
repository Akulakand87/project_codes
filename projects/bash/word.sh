#!/bin/bash

# List of words for the game
words=("apple" "banana" "cherry" "durian" "elderberry")

# Function to select a random word from the list
select_word() {
    local word_index=$((RANDOM % ${#words[@]}))
    echo "${words[$word_index]}"
}

# Function to check if the guessed letter is in the word
check_guess() {
    local word=$1
    local guess=$2

    if [[ $word == *"$guess"* ]]; then
        return 0
    else
        return 1
    fi
}

# Function to play the game
play_game() {
    local word=$(select_word)
    local guessed_letters=()
    local attempts=0

    echo "Welcome to the word guessing game!"
    echo "I'm thinking of a word. Can you guess it?"

    while true; do
        echo "Word: $(echo $word | sed "s/[^${guessed_letters[*]}]/_/g")"
        read -p "Guess a letter: " guess
        ((attempts++))

        if [[ $guess =~ ^[a-zA-Z]$ ]]; then
            if check_guess $word $guess; then
                guessed_letters+=($guess)
                if [[ $(echo $word | sed "s/[^${guessed_letters[*]}]/_/g") == $word ]]; then
                    echo "Congratulations! You guessed the word: $word"
                    echo "You took $attempts attempts to guess the word."
                    break
                fi
            else
                echo "Incorrect guess. Try again."
            fi
        else
            echo "Invalid input. Please enter a single letter."
        fi
    done
}

# Start the game
play_game
