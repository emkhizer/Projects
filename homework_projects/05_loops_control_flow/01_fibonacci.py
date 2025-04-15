# Constant for the maximum allowed Fibonacci term value
MAX_TERM_VALUE: int = 10000

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number

    print("🐇 Fibonacci Sequence up to", MAX_TERM_VALUE, ":\n")
    
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

    print("\n\n✅ Done!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
