def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')
    print()  # For a newline after printing all divisors

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()