def get_user_numbers():
    """
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """
    # Initialize an empty list to store the numbers entered by the user
    user_numbers = []
    
    # Start an infinite loop that will continue until manually broken
    while True:
        # Prompt the user to enter a number and store their input as a string
        user_input = input("Enter a number: ")
        
        # Check if the user entered a blank line (just pressed Enter)
        if user_input == "":
            # If the input is empty, exit the loop - this is our stopping condition
            break
        
        # If we get here, the user entered something
        # Convert the string input to an integer
        # Note: This will crash if the user enters non-numeric text
        num = int(user_input)
        
        # Add the integer to our list of numbers
        user_numbers.append(num)
    
    # After the loop exits, return the complete list of numbers
    return user_numbers


def count_nums(num_lst):
    """
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """
    # Initialize an empty dictionary to store the counts
    # Keys will be the numbers, values will be how many times they appear
    num_dict = {}
    
    # Loop through each number in the input list
    for num in num_lst:
        # Check if this number is already in our dictionary
        if num not in num_dict:
            # If it's not in the dictionary yet, add it with a count of 1
            # This handles the first occurrence of any number
            num_dict[num] = 1
        else:
            # If it's already in the dictionary, increment its count by 1
            # This handles subsequent occurrences of numbers
            num_dict[num] += 1
    
    # Return the completed dictionary of counts
    return num_dict


def print_counts(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """
    # Loop through each number (key) in the dictionary
    for num in num_dict:
        # For each number, print it along with its count from the dictionary
        # Convert both the number and count to strings for concatenation
        print(str(num) + " appears " + str(num_dict[num]) + " times.")
        # Note: An alternative, more modern way would be using f-strings:
        # print(f"{num} appears {num_dict[num]} times.")


def main():
    """
    Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of times each number appeared in the list.
    """
    # Step 1: Call the function to get numbers from the user
    user_numbers = get_user_numbers()
    
    # Step 2: Count how many times each number appears by calling count_nums
    num_dict = count_nums(user_numbers)
    
    # Step 3: Display the results by calling print_counts
    print_counts(num_dict)


# Python boilerplate - this ensures the main() function is only called when
# this script is run directly (not when imported as a module)
if __name__ == '__main__':
    main()