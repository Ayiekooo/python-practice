# sum_digits.py
# Add up the digits in a number.

def sum_digits(n):
    # make it positive and turn into string
    total = 0
    for ch in str(abs(n)):
        # convert each character back to int
        total += int(ch)
    return total

if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    print("Sum of digits is", sum_digits(n))
