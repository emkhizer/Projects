def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    # Check if it's a leap year using the Gregorian calendar rules:
    # 1. Divisible by 4
    # 2. If divisible by 100, must also be divisible by 400 to be a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # Condition explained:
        # - year % 4 == 0: The year must be divisible by 4
        # - year % 100 != 0: AND it should not be divisible by 100
        # - OR year % 400 == 0: UNLESS it's also divisible by 400
        print("That's a leap year!")
    else:
        print("That's not a leap year.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()