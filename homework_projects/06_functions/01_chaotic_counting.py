import random

DONE_LIKELIHOOD = 0.2  # Example value for the likelihood

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return  # This ends the function execution, so we'll get back to the main() function!
        print(i)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()