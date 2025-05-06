def average(a: float, b: float) -> float:
    """
    Returns the number which is half way between a and b.
    """
    return (a + b) / 2

def main():
    # Get user input for the first pair of numbers
    a1 = float(input("Enter the first number for the first pair: "))
    b1 = float(input("Enter the second number for the first pair: "))
    
    # Calculate the average of the first pair
    avg_1 = average(a1, b1)
    print(f"Average of {a1} and {b1} is: {avg_1}")
    
    # Get user input for the second pair of numbers
    a2 = float(input("Enter the first number for the second pair: "))
    b2 = float(input("Enter the second number for the second pair: "))
    
    # Calculate the average of the second pair
    avg_2 = average(a2, b2)
    print(f"Average of {a2} and {b2} is: {avg_2}")
    
    # Calculate the final average of the two averages
    final_avg = average(avg_1, avg_2)
    print(f"Final average of {avg_1} and {avg_2} is: {final_avg}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()