import random

def main():
    # Constants for the number of random numbers to generate and their range
    N_NUMBERS = 10
    MIN_VALUE = 1
    MAX_VALUE = 100
    
    # Generate and print 10 random numbers between 1 and 100
    for i in range(N_NUMBERS):
        # Generate a random number between MIN_VALUE and MAX_VALUE (inclusive)
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        
        # Print the number with a space after it (no newline)
        print(random_number, end=" ")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()