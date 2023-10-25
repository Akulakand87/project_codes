#!/bin/bash

# Generate a random number between 1 and 100
target=$((RANDOM % 100 + 1))

# Function to check if the guess is correct
check_guess() {
    local guess=$1

    if [[ $guess -eq $target ]]; then
        echo "Congratulations! You guessed the correct number."
        return 0
    elif [[ $guess -lt $target ]]; then
        echo "Too low. Try again."
    else
        echo "Too high. Try again."
    fi

    return 1
}

# Function to play the game
play_game() {
    local guess
    local attempts=0

    echo "Welcome to the guessing game!"
    echo "I'm thinking of a number between 1 and 100."

    while true; do
        read -p "Take a guess: " guess
        ((attempts++))

        if [[ $guess =~ ^[0-9]+$ ]]; then
            if check_guess $guess; then
                echo "You took $attempts attempts to guess the number."
                break
            fi
        else
            echo "Invalid input. Please enter a valid number."
        fi
    done
}

# Start the game
play_game
