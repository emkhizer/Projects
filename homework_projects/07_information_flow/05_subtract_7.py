def subtract_seven(num):
    """
    Subtracts 7 from the input number and returns the result.
    """
    return num - 7

def main():
    num = 7
    num = subtract_seven(num)
    print("This should be zero:", num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
