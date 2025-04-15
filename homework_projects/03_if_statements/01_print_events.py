def main():
    # Print the first 20 even numbers (0 through 38)
    for i in range(20):
        # The range(20) creates a sequence from 0 to 19 (20 numbers total)
        # This loop will execute exactly 20 times
        
        # Multiply i by 2 to get even numbers:
        # When i=0: 0*2=0
        # When i=1: 1*2=2
        # When i=2: 2*2=4
        # And so on until i=19: 19*2=38
        even_number = i * 2
        
        # Print each even number followed by a space instead of a newline
        # The "end=" " "" parameter replaces the default newline character
        # with a space, so all numbers appear on the same line
        print(even_number, end=" ")
        # Without end=" ", each number would print on a new line

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
    # This is a standard Python idiom that runs the main() function
    # when the script is executed directly (not imported)