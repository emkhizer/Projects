# Constant affirmation text
AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    # Initial prompt to the user
    print("Please type the following affirmation: " + AFFIRMATION)
    
    user_feedback = input()  # Get user's input
    
    # Loop until the input matches the affirmation
    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()  # Prompt again
    
    print("That's right! :)")  # Success message

# This provided line is required to call the main() function
if __name__ == '__main__':
    main()
