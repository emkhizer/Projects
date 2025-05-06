def count_even(lst):
    """
    Returns the number of even numbers in the list.
    >>> count_even([1, 2, 3, 4])
    2
    >>> count_even([1, 3, 5, 7])
    0
    """
    count = 0  # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0:  # If the current number in the list is even (divisible by 2)
            count += 1  # Add one to our count!
    print(count)  # Print out how many even numbers we counted above

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Make an empty list to store integers
    while True:
        user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
        if user_input == "":  # If the user presses enter
            break  # Exit the loop
        try:
            num = int(user_input)  # Cast the user input into an integer
            lst.append(num)  # Add the integer to our list
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()