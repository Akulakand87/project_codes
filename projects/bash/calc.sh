
#!/bin/bash

# Function to perform addition
addition() {
  echo "Enter the first number: "
  read num1
  echo "Enter the second number: "
  read num2
  result=$((num1 + num2))
  echo "The sum is: $result"
}

# Function to perform subtraction
subtraction() {
  echo "Enter the first number: "
  read num1
  echo "Enter the second number: "
  read num2
  result=$((num1 - num2))
  echo "The difference is: $result"
}

# Function to perform multiplication
multiplication() {
  echo "Enter the first number: "
  read num1
  echo "Enter the second number: "
  read num2
  result=$((num1 * num2))
  echo "The product is: $result"
}

# Function to perform division
division() {
  echo "Enter the dividend: "
  read dividend
  echo "Enter the divisor: "
  read divisor
  result=$((dividend / divisor))
  echo "The quotient is: $result"
}

# Main menu
echo "Welcome to the calculator!"
echo "Please select an operation:"
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"
read choice

case $choice in
  1)
    addition
    ;;
  2)
    subtraction
    ;;
  3)
    multiplication
    ;;
  4)
    division
    ;;
  *)
    echo "Invalid choice"
    ;;
esac