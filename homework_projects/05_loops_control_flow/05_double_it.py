def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Keep doubling the number while it's less than 100
    while curr_value < 100:
        doubled_value = curr_value * 2
        print(f"{curr_value} doubled is {doubled_value}")
        curr_value = doubled_value  # Update the value

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
