# even_odd.py
# Check if a number is even or odd.

def is_even(n):
    # even if no remainder when dividing by 2
    return n % 2 == 0

if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    if is_even(n):
        print(n, "is even")
    else:
        print(n, "is odd")
