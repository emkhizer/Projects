def main():
    # Define the minimum height requirement for the rollercoaster
    MINIMUM_HEIGHT = 50  # arbitrary units (cm, inches, etc.)
    
    # Ask the user for their height
    height = float(input("How tall are you? "))
    
    # Check if the user meets the height requirement
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()