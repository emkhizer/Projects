def double(num: int) -> int:
    """
    Returns the result of multiplying num by 2.
    
    Args:
    num (int): The number to be doubled.
    
    Returns:
    int: The result of num * 2.
    """
    return num * 2

# This is no need to edit code beyond this point
def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()