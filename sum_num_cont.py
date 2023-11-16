#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 16th, 2023
# this program asks the user for the number of numbers to add together.
# It then uses a while loop to repeatedly ask the user for a number to add.
# it will not accept invalid inputs.


def main() -> None:
    # Ask the user for the number of numbers to add together
    num_of_numbers = int(input("Enter the number of numbers to add together: "))

    # Initialize the current sum to 0
    current_sum = 0

    # Initialize a list to store the numbers added
    numbers_added = []

    # Use a WHILE loop to repeatedly ask the user for a number to add
    while num_of_numbers > 0:
        # Ask the user for a number to add
        number = input("Enter a number to add: ")

        try:
            # Convert the input to a float
            number = float(number)

            # Check if the number is a whole number
            if number.is_integer():
                # Add the whole number to the current sum
                current_sum += int(number)

                # Add the number to the list of numbers added
                numbers_added.append(int(number))
        except ValueError:
            # Invalid entry, skip adding the number
            print("Invalid entry. Please enter a valid number.")

        # Decrement the number of numbers left to add
        num_of_numbers -= 1

    # Display the numbers added
    print("Numbers added:", numbers_added)

    # Display the final sum
    print("Final sum:", current_sum)

    # Return the final sum
    return current_sum


if __name__ == "__main__":
    main()
