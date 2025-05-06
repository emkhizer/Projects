'''
Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """
'''


def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    return low <= n <= high


def main():
    # Sample test cases
    print("Test Case 1: in_range(5, 1, 10) →", in_range(5, 1, 10))  # True
    print("Test Case 2: in_range(0, 1, 10) →", in_range(0, 1, 10))  # False
    print("Test Case 3: in_range(10, 1, 10) →", in_range(10, 1, 10))  # True
    print("Test Case 4: in_range(1, 1, 10) →", in_range(1, 1, 10))  # True
    print("Test Case 5: in_range(11, 1, 10) →", in_range(11, 1, 10))  # False


if __name__ == "__main__":
    main()
