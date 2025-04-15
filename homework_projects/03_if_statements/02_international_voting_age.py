def main():
    # Define the voting age constants for each fictional country
    # These constants are defined at the top of the function for easy reference and modification
    PETURKSBOUIPO_AGE = 16  # Voting age in Peturksbouipo (like Scotland, Ethiopia, Austria)
    STANLAU_AGE = 25        # Voting age in Stanlau (like United Arab Emirates)
    MAYENGUA_AGE = 48       # Voting age in Mayengua (fictional, no real-world equivalent)

    # Prompt the user for their age and convert the input to an integer
    # The input() function collects text from the user
    # int() converts the text to an integer so we can compare it with the voting ages
    user_age = int(input("How old are you? "))
    # Note: This will crash if the user enters non-numeric input; error handling could be added

    # For each country, we check if the user's age meets the voting requirement
    # and print an appropriate message
    
    # Check for Peturksbouipo (voting age 16)
    if user_age >= PETURKSBOUIPO_AGE:
        # If the user's age is greater than or equal to 16, they can vote
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
        # Using f-string formatting to insert the voting age into the output message
    else:
        # If the user's age is less than 16, they cannot vote
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    
    # Check for Stanlau (voting age 25)
    if user_age >= STANLAU_AGE:
        # If the user's age is greater than or equal to 25, they can vote
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:
        # If the user's age is less than 25, they cannot vote
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")
    
    # Check for Mayengua (voting age 48)
    if user_age >= MAYENGUA_AGE:
        # If the user's age is greater than or equal to 48, they can vote
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        # If the user's age is less than 48, they cannot vote
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")


# This is a standard Python idiom that ensures the main() function 
# is only called when this script is run directly (not when imported)
if __name__ == '__main__':
    main()